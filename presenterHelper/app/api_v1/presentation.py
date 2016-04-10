__author__ = 'farzin'

from . import api
from . import app
from .. import db
from flask import jsonify, request,g
import json as js
import os
from ..decorators import json
from ..models import User,Presentation

@api.route('/users/<int:id>/create_presentation/', methods=['POST'])
@json
def create_presentation(id):

    req_data= request.json
    temp = req_data["name"]
    print(temp)
    user = User.query.get_or_404(id)
    presentation = Presentation(user=user)
    presentation.import_data(req_data)
    db.session.add(presentation)
    db.session.commit()
    return {}, 201, {'Location': presentation.get_url()}

@api.route('/get_presentation/<int:id>', methods=['GET'])
@json
def get_presentation(id):
    try:
       if(g.user):
           dir = os.path.join(app.config['DATA_DIR'], "user_"+str(g.user.user_id))
           file = open(dir+"/presentation_"+str(id))
           presentation = js.load(file)
           return presentation
       else:
            return jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    except IOError:
        return {"error":"the presentation not found"},404
