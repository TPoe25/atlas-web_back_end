#!/usr/bin/env python3
""" Auth module for API authentication
"""

import os
from flask import request
from typing import List, Optional


class Auth:
    """
    Template for all authentication systems.
    It provies methods for handling API authentication.
    """

    def require_auth(self, path: Optional[str],
                     excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication.

        Args:
            path (str or None): The request path.
            excluded_paths (list): Paths that don't require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if not excluded_paths or len(excluded_paths) == 0:
            return True

        # normalize path to always end with a slash
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return True

    def authorization_header(self, request=None) -> Optional[str]:
        """
        Retrieves the Authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str or None: The value of the Authorization header, or None if not.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> Optional[any]:
        """
        current user returns None

        Args:
            request: The Flask request object.

        Returns:
            None
        """
        return None

    def unauthorized(self) -> bool:
        """
        unauthorized returns True
        Returns:
            bool: Always True
        """
        return True

    def session_cookie(self, request=None):
        """
        Retrieves the session cookie from the request.

        Args:
            request: The Flask request object.
        Returns:
            The value of the session cookie, or None if not found.
        """
        if request is None:
            return None

        # Get the session name from environment variable or use default
        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None

        # Return the value of the session cookie
        return request.cookies.get(session_name)

