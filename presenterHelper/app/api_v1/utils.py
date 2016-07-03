from . import api
from . import app
import uuid
from flask import request, g, jsonify, url_for
import os
import json as js
from ..decorators import json
from ..auth import auth_token
import os


def allowed_file(extension):
    print(extension)
    print(app.config['ALLOWED_EXTENSIONS'])
    return extension in app.config['ALLOWED_EXTENSIONS']


"""
 @api {post} /upload Upload photo
 @apiName upload photo
 @apiGroup Utils

 @apiParam {File} imageFile Any image of .png, .jpg or .jpeg format

 @apiSuccess {json} filename the name of file in server is returned

 @apiSuccessExample {json} Success-Response:
                  {"filename": "10630a4e-0156-4734-8855-e01fd172173d.png"}

 @apiError {json} 406 the file format not supported
 @apiErrorExample {json} 406 Error-Response:
 {
    "error": "file type not supported"
 }
"""


@api.route('/upload', methods=['POST'])
@auth_token.login_required
def upload_image():
    if g.user:
        user_id = g.user.user_id
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        if file and allowed_file(extension):
            f_name = str(uuid.uuid4()) + extension
            directory = os.path.join(app.config['DATA_DIR2'], "user_" + str(user_id))
            if not os.path.exists(directory):
                os.mkdir(directory)
            file.save(os.path.join(directory, f_name))
            user_path = "user_"+ str(user_id)+"/"+f_name
            print(url_for('static', filename='img/'+user_path))
            img_url = url_for('static', filename='img/'+user_path)
            path = "http://154.16.156.58:8000"+img_url
            return js.dumps({'filename': path})
        else:
            return jsonify({"error": "file type not supported"}), 406


"""
 @api {get} /delete_image/image_name Delete image
 @apiName delete image
 @apiGroup Utils

 @apiParam {String} imageName name of image

 @apiSuccessExample {json} Success-Response:
                  {"msg": "image deleted successfully"}

 @apiError {json} 404 the image not found
 @apiErrorExample {json} 404 Error-Response:
 {
    "error": "the image not found"
 }
"""


@api.route('/delete_photo/<string:name>', methods=['GET'])
@auth_token.login_required
@json
def delete_image(name):
    if g.user:
        user_id = g.user.user_id
        directory = os.path.join(app.config['DATA_DIR'], "user_" + str(user_id))
        fname = os.path.join(directory, name)
        if not os.path.isfile(fname):
            return {"error": "the image not found"}, 404
        os.remove(fname)
        return {'msg': 'image deleted successfully'}, 200