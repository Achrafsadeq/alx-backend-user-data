#!/usr/bin/env python3
"""Session Database Authentication module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session Database Authentication class
    """

    def create_session(self, user_id: str = None) -> str:
        """Creates and stores a new session in database
        Args:
            user_id: The user ID to create session for
        Returns:
            The session ID if successful, None otherwise
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = super().create_session(user_id)
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves user ID associated with a session ID from database
        Args:
            session_id: The session ID to look up
        Returns:
            The user ID if found and valid, None otherwise
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        UserSession.load_from_file()
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return None

        user_session = user_sessions[0]
        if self.session_duration <= 0:
            return user_session.user_id

        if not hasattr(user_session, 'created_at'):
            return None

        expiration_time = user_session.created_at + timedelta(
            seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return user_session.user_id

    def destroy_session(self, request=None) -> bool:
        """Destroys a session from database
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

        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False

        user_session = user_sessions[0]
        user_session.remove()
        return True
