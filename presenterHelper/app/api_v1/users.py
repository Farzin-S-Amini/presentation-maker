from . import api
from ..models import User
from .. import db
from flask import jsonify, request
from ..email import send_email


def check_email_existance(email):
    if User.query.filter_by(email=email).first():
        return False
    return True


@api.route('/')
def say_hello():
    return jsonify({'msg': "hello world"})


@api.route('/register', methods=['POST'])
def register():
    req_data = request.json

    if not check_email_existance(req_data['email']):
        return jsonify({'error': 'this user already exists'}), 406

    user = User(req_data['email'], req_data['password'], req_data['firstname'], req_data['lastname'],
                req_data['is_audience'])

    db.session.add(user)
    db.session.commit()

    token = user.generate_confirmation_token()

    # send verification email here
    try:
        # this method should be modified
        send_email(user.email, 'register confirmation', None)
        print('email sent')
    except Exception as e:
        print(e)

    return jsonify({'msg': 'a confirmation message sent to user email' + str(token)}), 201


@api.route('/register_confirm/<token>', methods=['POST', 'GET'])
def register_confirm(token):
    user = User.verify_register_confirm_token(token)
    user.is_verified = True
    db.session.add(user)
    db.session.commit()

    # user should be redirected to login page in client
    return jsonify({'msg': 'user registration confirmed'}), 202
