#!/usr/bin/env python3
""" Main app module
"""
from flask import Flask, jsonify, request
from api.v1.views import app_views
from flask_cors import CORS
import os
from api.v1.auth.basic_auth import BasicAuth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
if os.getenv("AUTH_TYPE") == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()

@app.before_request
def before_request():
    """Handle authentication"""
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        return jsonify({"error": "Unauthorized"}), 401
    if auth.current_user(request) is None:
        return jsonify({"error": "Forbidden"}), 403
    request.current_user = auth.current_user(request)

@app.errorhandler(404)
def not_found(error) -> str:
    """404 not found"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "5000"))
    app.run(host=host, port=port)
