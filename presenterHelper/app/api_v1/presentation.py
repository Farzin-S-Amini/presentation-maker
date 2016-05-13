from . import api
from . import app
from .. import db
from flask import request, g
import os
from ..decorators import json
import json as js
from ..models import User, Presentation
from ..objectModels.PresentationModel import PresentationModel
from ..auth import auth_token


"""
 @api {post} git/create_presentation/ Request to create a presentation
 @apiName CreatePresentation
 @apiGroup Presentation

 @apiParam {String} name presentation name.

 @apiParamExample {json} Request-Example:
 {
    "name": "presentation name"
 }

 @apiSuccess {json} successMessage
 @apiSuccess {json} 201 message presentation creation message
 @apiSuccessExample {json} 201 Success-Response:
 {
    'presentation_id': 2
 }


 @apiError {json} 404 the User not found

"""


@api.route('/create_presentation', methods=['POST'])
@auth_token.login_required
@json
def create_presentation():
    if g.user:
        req_data = request.json
        user_id = g.user.user_id
        user = User.query.get_or_404(user_id)
        presentation = Presentation(user=user)
        presentation.import_data(req_data)
        db.session.add(presentation)
        db.session.flush()
        db.session.commit()
        return {'presentation_id': presentation.id}, 201


"""
 @api {get} /get_presentation/:id Request Presentation with id
 @apiName GetPresentation
 @apiGroup Presentation

 @apiParam {Number} id Presentation unique ID.

 @apiSuccess {json} presentation presentation content provided in a json file

 @apiError {json} 401 unauthorized
 @apiErrorExample {json} 401 Error-Response:
 {
    'error': 'unauthorized'
 }

 @apiError {json} 404 the presentation not found
 @apiErrorExample {json} 404 Error-Response:
 {
    "error": "the presentation not found"
 }
"""


@api.route('/get_presentation/<int:pid>', methods=['GET'])
@auth_token.login_required
@json
def get_presentation(pid):
    try:
        if g.user:
            directory = os.path.join(app.config['DATA_DIR'], "user_" + str(g.user.user_id))
            file = open(directory + "/presentation_" + str(pid))
            presentation = js.load(file)
            return presentation
        else:
            return {'error': 'unauthorized'}, 401
    except IOError:
        return {"error": "the presentation not found"}, 404


"""
 @api {get} /get_all_presentations/ Request all presentations of a user
 @apiName GetAllPresentations
 @apiGroup Presentation

 @apiSuccess {json} presentationList a list of presentations in json format

 @apiSuccessExample {json} Success-Response:
                   [{"id": 2, "name": "software engineering"}, {"id": 3, "name": "pres1"}]
"""

@api.route('/get_all_presentations/', methods=['GET'])
@auth_token.login_required
def get_all_presentations():
    if g.user:
        user_id = g.user.user_id
        user = User.query.get_or_404(user_id)
        p_list = list()
        for u in user.presentations:
            p = PresentationModel(u.id, u.name)
            p_list.append(p)
        json_string = js.dumps([ob.__dict__ for ob in p_list])
        print(json_string)
        return json_string
    else:
        return {'error': 'unauthorized'}, 401
    #
    #     directory = os.path.join(app.config['DATA_DIR'], "user_" + str(user_id))
    #     all_presentations = os.listdir(directory)
    #     presentations = list()
    #     for i in all_presentations:
    #         file = open(directory + '/' + i)
    #         presentations.append(js.load(file))
    #     c = C()
    #     c.list = presentations
    #     result = js.dumps(c.__dict__)
    #     return result

