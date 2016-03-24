__author__ = 'farzin'

import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, g

db = SQLAlchemy()

def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

     # apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    db.init_app(app)

    return app