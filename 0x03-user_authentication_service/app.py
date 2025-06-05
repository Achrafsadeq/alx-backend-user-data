#!/usr/bin/env python3
"""
Flask app for the authentication service.
This module implements a web service for user authentication with
registration, login, logout, and password reset functionality.
"""

from flask import Flask, jsonify, request, abort, make_response, redirect

from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Root endpoint that returns a welcome message.

    Returns:
        str: JSON response with welcome message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    Register a new user endpoint.

    Expected form data:
        email (str): User's email address
        password (str): User's password

    Returns:
        str: JSON response with registration result
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    User login endpoint.

    Expected form data:
        email (str): User's email address
        password (str): User's password

    Returns:
        str: JSON response with login result and session cookie
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = make_response(jsonify({"email": email, "message": "logged in"}))
    response.set_cookie("session_id", session_id)
    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """
    User logout endpoint.

    Expected cookie:
        session_id (str): User's session ID

    Returns:
        str: Redirect to root or 403 error
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """
    User profile endpoint.

    Expected cookie:
        session_id (str): User's session ID

    Returns:
        str: JSON response with user email or 403 error
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """
    Generate reset password token endpoint.

    Expected form data:
        email (str): User's email address

    Returns:
        str: JSON response with reset token or 403 error
    """
    email = request.form.get("email")

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """
    Update password endpoint.

    Expected form data:
        email (str): User's email address
        reset_token (str): Password reset token
        new_password (str): New password

    Returns:
        str: JSON response with update result or 403 error
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"})
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
