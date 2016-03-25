from flask import jsonify, g, current_app
from flask.ext.httpauth import HTTPBasicAuth
from .models import User

auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()



@auth.verify_password
def verify_password(username, password):
    g.user = User.query.filter_by(email=username).first()
    g.hasUser = True
    g.isVerified = True
    if g.user is None:
        g.hasUser = False
        return False
    if g.user.is_verified is False:
         g.isVerified = False
         return False
    return g.user.verify_password(password)

@auth.error_handler
def unauthorized():
    if g.hasUser is False:
         response = jsonify({'status': -200, 'error': 'userNotExist',
                        'message': 'please sign up'})
         return response
    if g.isVerified is False:
        response = jsonify({'status': -201, 'error': 'userNotVerified',
                        'message': 'please verify your email account'})
        return response

    response = jsonify({'status': -202, 'error': 'wrongPassword',
                        'message': 'The password is not correct'})
    response.status_code = -202
    return response

@auth_token.verify_password
def verify_auth_token(token, unused):
    if current_app.config.get('IGNORE_AUTH') is True:
        g.user = User.query.get(1)
    else:
        g.user = User.verify_auth_token(token)
    return g.user is not None

@auth_token.error_handler
def unauthorized_token():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    response.status_code = 401
    return response
