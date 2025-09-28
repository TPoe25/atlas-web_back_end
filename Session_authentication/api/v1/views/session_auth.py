#!/usr/bin/env python3
"""
Session authentication module
"""

from flask import request, jsonify, make_response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login():
    """
    Handle user login and create a session
    """
    from api.v1.app import auth

    # Validate email
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    # Validate password
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    # Wrong password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session for the user
    session_id = auth.create_session(user.id)
    user_json = user.to_json()

    # Set the session ID in a cookie
    session_name = os.getenv('SESSION_NAME')
    response  = make_response(jsonify(user_json))
    response.set_cookie(session_name, session_id)

    return response
