#!/usr/bin/env python3
"""
Auth module for authentication operations.
This module handles all authentication-related operations including
password hashing, user registration, login validation, and session management.
"""

import bcrypt
from typing import Union
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash a password with bcrypt.

    Args:
        password (str): The password to hash

    Returns:
        bytes: The salted hash of the password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a new UUID string.

    Returns:
        str: A string representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.

    This class provides methods for user authentication, registration,
    session management, and password reset functionality.
    """

    def __init__(self):
        """Initialize the Auth class with a database instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
            email (str): The user's email address
            password (str): The user's password

        Returns:
            User: The created user object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.

        Args:
            email (str): The user's email address
            password (str): The user's password

        Returns:
            bool: True if credentials are valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        """
        Create a new session for a user.

        Args:
            email (str): The user's email address

        Returns:
            Union[str, None]: The session ID if user exists, None otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Get a user by their session ID.
        """
        if session_id is None:
            return None

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroy a user's session.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        Generate a reset password token for a user.
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError(f"User {email} does not exist")

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Update a user's password using a reset token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(
                user.id,
                hashed_password=hashed_password,
                reset_token=None
            )
        except NoResultFound:
            raise ValueError("Invalid reset token")
