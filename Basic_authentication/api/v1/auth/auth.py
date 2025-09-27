#!/usr/bin/env python3
"""
Auth module for API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication.

        Returns True if:
        - path is None
        - excluded_paths is None or empty
        - path is NOT in excluded_paths (slash tolerant)

        Otherwise, returns False.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        """ Ensure trailing slash on path for slash-tolerant comparison """
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header returns None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user returns None """
        return None

    def unauthorized(self) -> bool:
        """ unauthorized returns True """
        return True

