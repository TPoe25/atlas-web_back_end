#!/usr/bin/env python3
""" Index module """

from flask import jsonify, abort
from . import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Status endpoint"""
    return jsonify({"status": "OK"})

@app_views.route('/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint that aborts with 401"""
    abort(401)
    return jsonify({"error": "Unauthorized"}), 401

@app_views.route('/unauthorized', methods=['GET'])
def forbidden():
    """Endpoint that aborts with 403"""
    abort(403)
    return jsonify({"error": "Forbidden"}), 403
