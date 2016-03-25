from . import api

@api.route('/')
def say_hello():
    return {'msg':"hello world"}

@api.route('/users', methods=['GET'])
def get_users():
    return "it is ok"


@api.route('/users/<int:id>', methods=['GET'])
def user(id):
    return id + " is ok"
