#!/usr/bin/env python3
"""Session Expiration Authentication module
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Session Authentication with Expiration class
    Implements session authentication with expiration functionality
    """

    def __init__(self):
        """Initialize SessionExpAuth instance
        Sets session_duration from environment variable or defaults to 0
        """
        try:
            self.session_duration = int(os.getenv('SESSION_DURATION', 0))
        except (ValueError, TypeError):
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """Creates a session with expiration tracking
        Args:
            user_id: User ID to create session for
        Returns:
            Session ID if successful, None otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets user ID from session ID with expiration check
        Args:
            session_id: Session ID to look up
        Returns:
            User ID if session is valid, None otherwise
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None

        if self.session_duration <= 0:
            return session_dict.get('user_id')

        created_at = session_dict.get('created_at')
        if created_at is None:
            return None

        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return session_dict.get('user_id')
