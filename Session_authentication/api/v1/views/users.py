#!/usr/bin/env python3
"""Module of Users views for the API."""
from api.v1.views import app_views
from flask import abort, jsonify, request
from flask.typing import ResponseReturnValue
from models.user import User
from typing import Optional, List, Dict


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> ResponseReturnValue:
    """Retrieve all users.

    Returns:
        JSON response with list of all User objects
    """
    all_users: List[Dict] = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str) -> ResponseReturnValue:
    """Retrieve a specific user by ID.

    Args:
        user_id: The ID of the user to retrieve

    Returns:
        JSON response with user data
        404 if user not found
    """
    if not user_id:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str) -> ResponseReturnValue:
    """Delete a user by ID.

    Args:
        user_id: The ID of the user to delete

    Returns:
        Empty JSON response if successful
        404 if user not found
    """
    if not user_id:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> ResponseReturnValue:
    """Create a new user.

    Expected JSON body:
        - email: required
        - password: required
        - first_name: optional
        - last_name: optional

    Returns:
        JSON response with created user data
        400 if creation fails
    """
    try:
        rj = request.get_json()
    except Exception:
        rj = None

    error_msg = None
    if rj is None:
        error_msg = "Wrong format"
    elif not rj.get("email"):
        error_msg = "email missing"
    elif not rj.get("password"):
        error_msg = "password missing"

    if error_msg is None:
        try:
            user = User()
            user.email = rj.get("email")
            user.password = rj.get("password")
            user.first_name = rj.get("first_name")
            user.last_name = rj.get("last_name")
            user.save()
            return jsonify(user.to_json()), 201
        except Exception as e:
            error_msg = f"Can't create User: {str(e)}"

    return jsonify({'error': error_msg}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str) -> ResponseReturnValue:
    """Update a user's information.

    Args:
        user_id: The ID of the user to update

    Expected JSON body:
        - first_name: optional
        - last_name: optional

    Returns:
        JSON response with updated user data
        404 if user not found
        400 if update fails
    """
    if not user_id:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)

    try:
        rj = request.get_json()
    except Exception:
        return jsonify({'error': "Wrong format"}), 400

    if rj is None:
        return jsonify({'error': "Wrong format"}), 400

    if rj.get('first_name') is not None:
        user.first_name = rj.get('first_name')
    if rj.get('last_name') is not None:
        user.last_name = rj.get('last_name')

    user.save()
    return jsonify(user.to_json()), 200

@app_views.route('/users/<user_id>/', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Get a user by ID.

    Args:
        user_id (str): The ID of the user to retrieve.

    """
    if user_id == 'me':
       user = getattr(request, 'current_user', None)
       if user is None:
           abort(404)
       return jsonify(user.to_json())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json()), 200
