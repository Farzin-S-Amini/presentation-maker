from flask import Blueprint
from .. import current_app as app
from ..decorators import etag, rate_limit

api = Blueprint('api', __name__)


@api.before_request
#@rate_limit(limit=5, period=15)
def before_request():
    """All routes in this blueprint require authentication."""
    pass


@api.after_request
# @etag
def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv


from . import users, presentation, utils, edit_presentation_events, presentation_events, presenter_page_events, session
