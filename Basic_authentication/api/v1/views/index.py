#!/usr/bin/env python3
""" Index module """

from flask import jsonify, abort
from . import app_views

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """Get /api/v1/status """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats() -> str:
    """Get /api/v1/stats """
    from models.user import User
    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route() -> str:
    """ GET /api/v1/unauthorized """
    abort(401)

@app_views.route('/forbidden', methods=['GET'])
def forbidden() -> str:
    """Endpoint that aborts with 403"""
    abort(403)
    return jsonify({"error": "Forbidden"}), 403
