from . import api
from ..models import User
from .. import db
from flask import jsonify, request, redirect
from ..email import send_email


def check_email_existence(email):
    if User.query.filter_by(email=email).first():
        return False
    return True


@api.route('/')
def say_hello():
    return jsonify({'msg': "hello world"})


"""
 @api {post} /register register a user
 @apiName Register
 @apiGroup User

 @apiParamExample {json} Request-Example:
 {
    "email": "ehsanroman74@gmail.com",
    "password": "asdfgh",
    "firstname": "ehsan",
    "lastname": "golshani",
    "is_audience": false
 }

 @apiSuccess {json} 201 message register confirmation message
 @apiSuccessExample {json} 201 Success-Response:
 {
    'msg': 'a confirmation message sent to user email'
 }

 @apiError {json} 406 user already exists
 @apiErrorExample {json} 406 Error-Response:
 {
    'error': 'this user already exists'
 }

 @apiError {json} 401 confirmation email did not send
 @apiErrorExample {json} 401 Error-Response:
 {
    'error': 'problem with sending email'
 }
"""


@api.route('/register', methods=['POST'])
def register():
    req_data = request.json

    if not check_email_existence(req_data['email']):
        return jsonify({'error': 'this user already exists'}), 406

    user = User(req_data['email'], req_data['password'], req_data['firstname'], req_data['lastname'],
                req_data['is_audience'])
    user.is_verified = True
    db.session.add(user)
    db.session.commit()

    token = user.generate_confirmation_token()

    # send verification email here
    try:
        # this method should be modified
        send_email(user.email, 'register confirmation',
                   "http://localhost:8000/api/v1/register_confirm/" + str(token), None)
        print('registeration confirmation email sent  ' + str(token))
        return jsonify({'msg': 'a confirmation message sent to user email'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': 'problem with sending email'}), 401


@api.route('/register_confirm/<token>', methods=['GET'])
def register_confirm(token):
    user = User.verify_register_confirm_token(token)
    user.is_verified = True
    db.session.add(user)
    db.session.commit()

    # user should be redirected to login page in client
    return redirect("file:///home/farzin/Desktop/SE-Front/rgs.html", code=302)


"""
 @api {get} /forget-password/:email respond to forget password request
 @apiName ForgetPassword
 @apiGroup User


 @apiSuccess {json} 201 forgot message confirmation message
 @apiSuccessExample {json} 201 Success-Response:
 {
    'msg': 'change password link has been send to your email'
 }


 @apiError {json} 404 user does not exist
 @apiErrorExample {json} 404 Error-Response:
 {
    'error': 'this user does not exists'
 }

 @apiError {json} 406 email did not send
 @apiErrorExample {json} 406 Error-Response:
 {
    'error': 'problem with sending email'
 }
"""


@api.route('/forget-password/<string:email>', methods=['GET'])
def forget_password(email):
    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({'error': 'this user does not exists'}), 404

    token = user.generate_email_token()

    # send forget password email here
    try:
        # this method should be modified
        send_email(email, 'forgot password',
                   "file:///home/farzin/Desktop/SE-Front/updatepass.html" + str(token), None)
        print('forgot password email sent : ' + str(token))
        return jsonify({'msg': 'change password link has been send to your email'}), 201
    except Exception as e:
        print(e)
        return jsonify({'error': 'problem with sending email'}), 406


"""
 @api {post} /change-password/:token update user password
 @apiName UpdatePassword
 @apiGroup User

 @apiParam {string} password new password
 @apiParamExample {json} Request-Example:
 {
    "password": "asdfgh"
 }

 @apiSuccess {json} 202 change user password confirmation message
 @apiSuccessExample {json} 202 Success-Response:
 {
    'msg': 'user password changed successfully'
 }

 @apiError {json} 406 user already exists
 @apiErrorExample {json} 406 Error-Response:
 {
    'error': 'this user already exists'
 }
"""


@api.route('/change-password/<token>', methods=['POST'])
def update_password(token):
    req_data = request.json

    user = User.verify_email_token(token=token)

    if user is None:
        return jsonify({'error': 'this user does not exist'}), 406

    user.set_password(req_data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'user password changed successfully'}), 202
