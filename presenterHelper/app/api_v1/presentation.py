from . import api
from . import app
from .. import db
from flask import request, g
import os
from ..decorators import json
import json as js
from ..models import User, Presentation

"""
 @api {post} /users/:id/create_presentation/ Request to create a presentation
 @apiName CreatePresentation
 @apiGroup Presentation

 @apiParam {Number} id User unique ID.

 @apiParamExample {json} Request-Example:
 {
    "name": "new presentation"
 }

 @apiSuccess {json} presentationLocation the location of new presentation in server

 @apiError {json} 404 the User not found

"""


@api.route('/users/<int:id>/create_presentation/', methods=['POST'])
@json
def create_presentation(id):
    req_data = request.json
    temp = req_data["name"]
    print(temp)
    user = User.query.get_or_404(id)
    presentation = Presentation(user=user)
    presentation.import_data(req_data)
    db.session.add(presentation)
    db.session.commit()
    return {'Location': presentation.get_url()}, 201


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


@api.route('/get_presentation/<int:id>', methods=['GET'])
@json
def get_presentation(id):
    try:
        if g.user:
            directory = os.path.join(app.config['DATA_DIR'], "user_" + str(g.user.user_id))
            file = open(directory + "/presentation_" + str(id))
            presentation = js.load(file)
            return presentation
        else:
            return {'error': 'unauthorized'}, 401
    except IOError:
        return {"error": "the presentation not found"}, 404


class C:
    pass


"""
 @api {get} /users/:id/get_all_presentations/ Request Presentation with id
 @apiName GetAllPresentations
 @apiGroup Presentation

 @apiParam {Number} id User unique ID.

 @apiSuccess {json} presentationList a list of presentations in json format

"""


@api.route('/users/<int:id>/get_all_presentations/', methods=['GET'])
def get_all_presentations(id):
    directory = os.path.join(app.config['DATA_DIR'], "user_" + str(id))
    all_presentations = os.listdir(directory)
    presentations = list()
    for i in all_presentations:
        file = open(directory + '/' + i)
        presentations.append(js.load(file))
    c = C()
    c.list = presentations
    result = js.dumps(c.__dict__)
    return result
