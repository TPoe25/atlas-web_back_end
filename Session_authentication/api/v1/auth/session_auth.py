#!/usr/bin/env python3
"""
Session authentication module
"""

from api.v1.auth.auth import Auth
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
            str: The user ID associated with the session ID or None if not found
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

