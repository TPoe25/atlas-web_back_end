#!/usr/bin/env python3
"""Route module for the API"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(401)
def unauthorized(error: HTTPException):
    """
    Unauthorized handler
    Args:
        error: HTTP exception object
    Returns:
        tuple: JSON response and 401 status code
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error: HTTPException):
    """
    Forbidden handler
    Args:
        error: HTTP exception object
    Returns:
        tuple: JSON response and 403 status code
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error: HTTPException):
    """
    Not found handler
    Args:
        error: HTTP exception object
    Returns:
        tuple: JSON response and 404 status code
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = int(getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
