from . import api



@api.route('/')
def say_hello():
    return {'msg':"hello world"}


