__author__ = 'farzin.amini@gmail.com'

from . import api
from .. import db
from ..auth import auth_token
from ..models import Presentation, Session, User
from ..decorators import json
from flask import g, request
from ..objectModels.SessionModel import SessionModel
import string, random
import json as js


"""
 @api {post} /create_session/ Request to create a session
 @apiName CreateSession
 @apiGroup Session

 @apiParam {Integer} pid presentation id.

 @apiParamExample {json} Request-Example:
 {
    "pid" : "2"
 }


 @apiSuccess {json} session_code session entrance code
 @apiSuccessExample {json} 200 Success-Response:
 {
    'session_code': 'W2GSA'
 }


 @apiError {json} 404 the User not found

"""

@api.route("/create_session", methods=["POST"])
@auth_token.login_required
@json
def create_session():
    if g.user:
        req_data = request.json
        user_id = g.user.user_id
        pid = req_data['pid']
        presentation = Presentation.query.get_or_404(pid)
        session = Session(presentation=presentation)
        code = generate_session_code()
        session.import_data(req_data, pid, code)
        db.session.add(session)
        db.session.commit()
        return {'session_code': code}, 200


def generate_session_code():
    size = 5
    chars = string.ascii_uppercase + string.digits
    code = ""
    condition = True
    while condition:
        code = ''.join(random.choice(chars) for _ in range(size))
        condition = not is_code_unique(code)
    return code


def is_code_unique(code):
    sessions = Session.query.filter_by(is_active=True).all()
    for i in sessions:
        if code == i.code:
            return False
    return True


"""
 @api {post} /join_session/ Request to join a session
 @apiName JoinSession
 @apiGroup Session

 @apiParam {String} code session code.

 @apiParamExample {json} Request-Example:
 {
    "code" : "WX1RQ"
 }

 @apiSuccess {json} 201 message session joined successfully
 @apiSuccessExample {json} 201 Success-Response:
 {
    'message': 'participant joined successfully'
 }


 @apiError {json} 404 the User not found

"""


@api.route("/join_session", methods=["POST"])
@auth_token.login_required
@json
def join_session():
    if g.user:
        req_data = request.json
        user_id = g.user.user_id
        user = User.query.get_or_404(user_id)
        session_code = req_data['code']
        session = Session.query.filter_by(is_active=True, code=session_code).first()
        session.participants.append(user)
        db.session.commit()
        return {'message': 'participant joined successfully'}, 201

"""
 @api {Get} /get_sessions/uid Request to get all sessions of a presenter
 @apiName GetSessions
 @apiGroup Session

 @apiParam {Number} uid presenter id.


 @apiSuccessExample {json} 201 Success-Response:
 {
 "current_page": 0, "is_active": true, "end_date": null, "presentation_name": "computer","name": "firstSession", "code": "8X5XV"
 }


 @apiError {json} 404 the User not found

"""


@api.route("/get_sessions/<int:uid>", methods=["GET"])
@auth_token.login_required
def get_sessions(uid):
	if g.user:
		session = Session.query.filter_by(presenter_id=uid).first()
		p_name = Presentation.query.filter_by(id=session.presentation_id).first().name
		session_model = SessionModel(session,p_name)
		json_session = js.dumps(session_model.__dict__)
		return json_session