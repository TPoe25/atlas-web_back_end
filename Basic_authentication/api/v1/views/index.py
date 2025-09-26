#!/usr/bin/env python3
""" Index view module """
from flask import jsonify
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """ Returns a JSON status response """
    return jsonify({"status": "OK"})
