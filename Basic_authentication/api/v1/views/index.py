from flask import jsonify, abort
from api.v1.views import app_views

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized():
    """Endpoint that raises a 401 Unauthorized error"""
    abort(401)
