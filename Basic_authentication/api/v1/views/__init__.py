from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

"""API authentication module.
"""
from api.v1.views import index
from api.v1.views import users
from api.v1 import auth
