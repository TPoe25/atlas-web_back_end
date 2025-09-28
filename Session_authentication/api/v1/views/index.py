#!/usr/bin/env python3
"""Module of Index views."""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return status of API.

    Returns:
        JSON response with status OK
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Get statistics about objects.

    Returns:
        JSON response with count of objects
    """
    from models.user import User
    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """Endpoint that returns 401 error.

    Returns:
        JSON response with unauthorized error
    """
    return jsonify({"error": "Unauthorized"}), 401


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """Endpoint that returns 403 error.

    Returns:
        JSON response with forbidden error
    """
    return jsonify({"error": "Forbidden"}), 403
