#!/usr/bin/env python3
"""
Session authentication module
"""

from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session authentication class inheriting from Auth
    """

    # Dictionary to store session ID to user ID mapping
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for a given user ID
        Args:
            user_id (str): The user ID for which to create a session
        Returns:
            str: The created session ID or None if user_id not a string
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique session ID
        session_id = str(uuid.uuid4())

        # Map the session ID to the user ID
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieve the user ID associated with a given session ID
        Args:
            session_id (str): The session ID for which to retrieve the user ID
        Returns:
            str: The user ID associated w/ the session ID or None if not found
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retrieve the current user based on the session ID from the request
        Args:
            request: The HTTP request object
        Returns:
            The user object associated with the session ID or None if not found
        """
        if request is None:
            return None

        # Get the session ID from the request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Find the user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Get the user object using the user ID
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Destroy the session associated with the request
        Args:
            request: The HTTP request object
        Returns:
            bool: True if session was successfully destroyed, False otherwise
        """
        if request is None:
            return False

        # Get the session ID from the request cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Find the user ID associated with the session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Remove the session ID to user ID mapping
        try:
            del self.user_id_by_session_id[session_id]
        except KeyError:
            return False

        return True
