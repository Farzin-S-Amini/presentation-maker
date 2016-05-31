# presentation sockets

from .. import socketio
from . import app
from ..models import Session
from .. import db
import json as js
import os
from flask import session
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect


@socketio.on('change page', namespace='/presentation')
def change_page(data, room_name):
    print(data['page'])
    session = Session.query.filter_by(code=room_name, is_active=True)
    session.current_page = data['page']
    db.session.commit()
    emit('page changed', {'page': data['page']}, room=room_name)


@socketio.on('end session', namespace='/presentation')
def end_session(room_name):
    try:
        session = Session.query.filter_by(code=room_name, is_active=True)
        session.is_active = False
        db.session.commit()

        print("session ended")
        emit('session ended', room=room_name)
        return 1
    except Exception as e:
        print(e)
        return 0


##############################################################################

@socketio.on('connect', namespace='/presentation')
def test_connect():
    emit('my response', {'data': 'Connected'},)


@socketio.on('disconnect', namespace='/presentation')
def test_disconnect():
    print('Client disconnected')


@socketio.on('my event', namespace='/presentation')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event', namespace='/presentation')
def test_broadcast_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('join', namespace='/presentation')
def join(message):
    try:
        # get presentation json file using room
        # session = Session.query.filter_by(code=message['room'], is_active=True).first()
        # pid = session.presentation.id
        # user_id = session.presenter_id
        # page_number = session.current_page
        # directory = os.path.join(app.config['DATA_DIR'], "user_" + str(user_id))
        # file = open(directory + "/presentation_" + str(pid))
        # presentation_file = js.load(file)
        join_room(message['room'])
        emit('my response', {"data": "sb joined"}, room=message['room'])
        # emit('init presentation', {"json": presentation_file, "page": page_number})
        emit('init presentation', {"json": "asa", "page": 2})
        return 1
    except Exception as e:
        print(e)
        return 0


@socketio.on('send answer', namespace='/presentation')
def send_answer(message):
    # do some things here
    print(message)
    emit('catch answer', {"answer": message['answer'], "page": message['page']}, room=message['room'])


@socketio.on('leave', namespace='/presentation')
def leave(message):
    leave_room(message['room'])
    emit('my response', {'data': 'In rooms: ' + ', '.join(rooms())})


@socketio.on('close room', namespace='/presentation')
def close(message):
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.'}, room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/presentation')
def send_room_message(message):
    emit('my response', {'data': message['data']}, room=message['room'])


@socketio.on('disconnect request', namespace='/presentation')
def disconnect_request():
    emit('my response', {'data': 'Disconnected!'})
    disconnect()
