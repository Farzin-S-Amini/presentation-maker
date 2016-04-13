import os

from flask import Flask, jsonify, g, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from .decorators import json, no_cache, rate_limit
from flask.ext.mail import Mail
from flask_socketio import SocketIO
from flask.ext.cors import CORS

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on available packages.

async_mode = None

if async_mode is None:
    try:
        import eventlet

        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey

            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet

    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey

    monkey.patch_all()

thread = None

db = SQLAlchemy()
mail = Mail()
socketio = SocketIO(async_mode=async_mode)


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)
    CORS(app)
    # apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # register blueprints
    from .api_v1 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    # register an after request handler
    @app.after_request
    def after_request(rv):
        headers = getattr(g, 'headers', {})
        rv.headers.extend(headers)
        return rv

    # authentication token route
    from .auth import auth
    @app.route('/get-auth-token')
    @auth.login_required
    @rate_limit(1, 600)  # one call per 10 minute period
    @no_cache
    @json
    def get_auth_token():
        return {'token': g.user.generate_auth_token()}

    socketio.init_app(app)

    return app

# import app
#
# if not app.debug:
#     import logging
#     from logging.handlers import RotatingFileHandler
#     file_handler = RotatingFileHandler('tmp/presentation-maker.log', 'a', 1 * 1024 * 1024, 10)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('presentation-maker startup')
