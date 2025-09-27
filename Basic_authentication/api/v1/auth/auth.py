#!/usr/bin/env python3
""" Auth module for API authentication
"""

from typing import List, Optional

class Auth:
    """
    Template for all authentication systems.
    It provies methods for handling API authentication.
    """

    def require_auth(self, path: Optional[str], excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication.

        Args:
            path (str or None): The request path.
            excluded_paths (list): List of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Ensure trailing slash on path for slash-tolerant comparison
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if not excluded.endswith('/'):
                excluded += '/'
            if excluded == path:
                return False

        return True

    def authorization_header(self, request=None) -> Optional[str]:
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

    def current_user(self, request=None) -> Optional[Any]:
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
