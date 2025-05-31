#!/usr/bin/env python3
"""User Session module for storing session data in database
"""
from models.base import Base


class UserSession(Base):
    """User Session class that stores session data in database
    """

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a new UserSession instance
        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
