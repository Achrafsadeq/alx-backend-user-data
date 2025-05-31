#!/usr/bin/env python3
"""Module of Users views
Handles all RESTful API actions for User objects
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """GET /api/v1/users
    Retrieves the list of all User objects
    Requires Basic Authentication
    Returns:
        - JSON list of all User objects
        - 401 if unauthorized
        - 403 if forbidden
    """
    from api.v1.auth import auth

    if auth is None:
        return jsonify({"error": "Unauthorized"}), 401

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """GET /api/v1/users/<user_id>
    Retrieves a specific User object
    Args:
        user_id: ID of the User to retrieve
    Returns:
        - JSON representation of the User
        - 404 if User doesn't exist
        - 401 if unauthorized
        - 403 if forbidden
    """
    from api.v1.auth import auth

    if auth is None:
        return jsonify({"error": "Unauthorized"}), 401

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def view_current_user() -> str:
    """GET /api/v1/users/me
    Retrieves the currently authenticated User
    Returns:
        - JSON representation of the current User
        - 401 if unauthorized
    """
    from api.v1.auth import auth

    if auth is None:
        return jsonify({"error": "Unauthorized"}), 401

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    return jsonify(current_user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """DELETE /api/v1/users/<user_id>
    Deletes a User object
    Args:
        user_id: ID of the User to delete
    Returns:
        - Empty JSON response
        - 404 if User doesn't exist
        - 401 if unauthorized
        - 403 if forbidden
    """
    from api.v1.auth import auth

    if auth is None:
        return jsonify({"error": "Unauthorized"}), 401

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """POST /api/v1/users/
    Creates a new User
    JSON Body:
        - email: user's email
        - password: user's password
        - first_name: optional first name
        - last_name: optional last name
    Returns:
        - JSON representation of new User
        - 400 if invalid input
    """
    rj = None
    error_msg = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        error_msg = "Wrong format"
    if error_msg is None and rj.get("email", "") == "":
        error_msg = "email missing"
    if error_msg is None and rj.get("password", "") == "":
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
            error_msg = "Can't create User: {}".format(e)
    return jsonify({'error': error_msg}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """PUT /api/v1/users/<user_id>
    Updates a User object
    Args:
        user_id: ID of the User to update
    JSON Body:
        - first_name: optional new first name
        - last_name: optional new last name
    Returns:
        - JSON representation of updated User
        - 404 if User doesn't exist
        - 400 if invalid input
        - 401 if unauthorized
        - 403 if forbidden
    """
    from api.v1.auth import auth

    if auth is None:
        return jsonify({"error": "Unauthorized"}), 401

    auth_header = auth.authorization_header(request)
    if auth_header is None:
        abort(401)

    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    if user_id is None:
        abort(404)
    user = User.get(user_id)
    if user is None:
        abort(404)
    rj = None
    try:
        rj = request.get_json()
    except Exception as e:
        rj = None
    if rj is None:
        return jsonify({'error': "Wrong format"}), 400
    if rj.get('first_name') is not None:
        user.first_name = rj.get('first_name')
    if rj.get('last_name') is not None:
        user.last_name = rj.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
