#!/usr/bin/env python3
""" views for User object
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a User object by ID"""
    if user_id == "me":
        if not hasattr(request, 'current_user') or request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_json())

    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())
