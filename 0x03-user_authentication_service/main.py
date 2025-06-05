#!/usr/bin/env python3
"""
End-to-end integration test for the authentication service.
This module tests all endpoints of the authentication service
to ensure they work correctly together.
"""

import requests
from typing import Union


def register_user(email: str, password: str) -> None:
    """
    Test user registration endpoint.

    Args:
        email (str): User's email address
        password (str): User's password
    """
    url = "http://0.0.0.0:5000/users"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Test login with wrong password.

    Args:
        email (str): User's email address
        password (str): Wrong password
    """
    url = "http://0.0.0.0:5000/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Test user login endpoint.

    Args:
        email (str): User's email address
        password (str): User's password

    Returns:
        str: The session ID cookie value
    """
    url = "http://0.0.0.0:5000/sessions"
    data = {"email": email, "password": password}
    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}

    return response.cookies.get("session_id")


def profile_unlogged() -> None:
    """Test profile access without login."""
    url = "http://0.0.0.0:5000/profile"
    response = requests.get(url)

    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Test profile access with valid session.

    Args:
        session_id (str): Valid session ID
    """
    url = "http://0.0.0.0:5000/profile"
    cookies = {"session_id": session_id}
    response = requests.get(url, cookies=cookies)

    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """
    Test user logout endpoint.

    Args:
        session_id (str): Valid session ID
    """
    url = "http://0.0.0.0:5000/sessions"
    cookies = {"session_id": session_id}
    response = requests.delete(url, cookies=cookies)

    assert response.status_code == 200


def reset_password_token(email: str) -> str:
    """
    Test reset password token generation.

    Args:
        email (str): User's email address

    Returns:
        str: The reset token
    """
    url = "http://0.0.0.0:5000/reset_password"
    data = {"email": email}
    response = requests.post(url, data=data)

    assert response.status_code == 200
    assert "reset_token" in response.json()

    return response.json()["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Test password update endpoint.

    Args:
        email (str): User's email address
        reset_token (str): Valid reset token
        new_password (str): New password
    """
    url = "http://0.0.0.0:5000/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(url, data=data)

    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
