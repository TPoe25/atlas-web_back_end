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

        Args:
            path (str): The request path.
            excluded_paths (List[str]): List of paths excluded from auth.

        Returns:
            bool: False by default
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns the value of the Authorization header.

        Args:
            request: Flask request object.

        Returns:
            str: None by default
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user.

        Args:
            request: Flask request object.

        Returns:
            User: None by default
        """
        return None
