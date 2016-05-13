# presentation sockets

from .. import socketio
from . import app
from flask import session, request
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect


@socketio.on('change page', namespace='/presentation')
def change_page(data):
    print(data['page'])
    emit('page changed', {'page': data['page']}, broadcast=True)


@socketio.on('end session', namespace='/presentation')
def end_session():
    try:
        # do what is needed in server when the session in ending
        print("session ended")
        emit('session ended', broadcast=True)
        return 1
    except Exception as e:
        print(e)
        return 0


##############################################################################

@socketio.on('connect', namespace='/presentation')
def test_connect():
    emit('my response', {'data': 'Connected'})


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
    join_room(message['room'])
    emit('my response', {'data': 'In rooms: ' + ', '.join(rooms())})


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
