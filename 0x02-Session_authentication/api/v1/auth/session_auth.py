#!/usr/bin/env python3
"""Session Authentication module for API
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session Authentication class that implements session-based auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a given user_id
        Args:
            user_id: The user ID to create session for
        Returns:
            The session ID if successful, None otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user ID associated with a session ID
        Args:
            session_id: The session ID to look up
        Returns:
            The user ID if found, None otherwise
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Retrieves the current user based on session cookie
        Args:
            request: The Flask request object
        Returns:
            The User object if found, None otherwise
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Destroys an authenticated session
        Args:
            request: The Flask request object
        Returns:
            True if session was destroyed, False otherwise
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
