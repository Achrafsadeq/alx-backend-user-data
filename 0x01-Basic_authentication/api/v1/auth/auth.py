#!/usr/bin/env python3
"""
Auth module for API authentication management
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template class for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Args:
            path: The request path to check
            excluded_paths: List of paths that don't require authentication

        Returns:
            True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path by ensuring it ends with /
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            # Handle wildcard patterns
            if excluded_path.endswith('*'):
                if normalized_path.startswith(excluded_path[:-1]):
                    return False
            else:
                # Normalize excluded path
                normalized_excluded = excluded_path
                if excluded_path.endswith('/') else excluded_path + '/'
                if normalized_path == normalized_excluded:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request

        Args:
            request: Flask request object

        Returns:
            Authorization header value or None
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request

        Args:
            request: Flask request object

        Returns:
            User object or None
        """
        return None
