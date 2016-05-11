# edit presentation sockets

from .. import socketio
from . import app
from flask import session, request
from flask_socketio import emit, join_room, leave_room, \
    close_room, rooms, disconnect
import os
from io import StringIO
from io import BytesIO
import re
from PIL import Image
import uuid
import base64

import json as js


@socketio.on('update presentation', namespace='/edit_presentation')
def update_presentation(json, user_id, presentation_id):
    try:
        directory = os.path.join(app.config['DATA_DIR'], "user_" + str(user_id))
        if not os.path.exists(directory):
            os.mkdir(directory)
        file = open(directory + "/presentation_" + str(presentation_id), 'w')
        file.write(json)
        file.close()
        print('file saved in server')
        return 1
    except Exception as e:
        print(e)
        return 0


@socketio.on('save image', namespace='/edit_presentation')
def save_image(message):
    image_data = re.sub('^data:image/png;base64,', '', message['data'])
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    if image:
        f_name = str(uuid.uuid4()) + ".png"
        directory = os.path.join(app.config['DATA_DIR'], "user_" + str(1))
        if not os.path.exists(directory):
            os.mkdir(directory)
        image.save(os.path.join(directory, f_name))
        emit('my response', {'data': f_name})


#########################################################################################################
@socketio.on('connect', namespace='/edit_presentation')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/edit_presentation')
def test_disconnect():
    print('Client disconnected')


@socketio.on('my event', namespace='/edit_presentation')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response', {'data': message['data']})


@socketio.on('my broadcast event', namespace='/edit_presentation')
def test_broadcast_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('join', namespace='/edit_presentation')
def join(message):
    join_room(message['room'])
    emit('my response', {'data': 'In rooms: ' + ', '.join(rooms())})


@socketio.on('leave', namespace='/edit_presentation')
def leave(message):
    leave_room(message['room'])
    emit('my response', {'data': 'In rooms: ' + ', '.join(rooms())})


@socketio.on('close room', namespace='/edit_presentation')
def close(message):
    emit('my response', {'data': 'Room ' + message['room'] + ' is closing.'}, room=message['room'])
    close_room(message['room'])


@socketio.on('my room event', namespace='/edit_presentation')
def send_room_message(message):
    emit('my response', {'data': message['data']}, room=message['room'])


@socketio.on('disconnect request', namespace='/edit_presentation')
def disconnect_request():
    emit('my response', {'data': 'Disconnected!'})
    disconnect()
