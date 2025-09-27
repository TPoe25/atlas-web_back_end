#!/usr/bin/env python3
"""
Auth module for API authentication
"""

from flask import Request
from typing import List, Optional, Any


class Auth:
    """
    Template for all authentication systems.
    """

    def require_auth(self, path: Optional[str], excluded_paths: List[str]) -> bool:
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

        """
        Ensure trailing slash on path for slash-tolerant comparison
        """
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded == path:
                return False

        return True

    def authorization_header(self, request: Optional[Any] = None) -> Optional[str]:
        """
        Retrieves the Authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str or None: The value of the Authorization header, or None if not present.
        """
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self , request: None):
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
