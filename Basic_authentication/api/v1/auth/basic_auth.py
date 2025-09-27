#!/usr/bin/env python3
"""
Basic authentication module
"""

import base64
from models.user import User
from typing import Optional
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class
    """
    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               Optional[str]) -> Optional[str]:
        """Decode the Base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_base64_authorization_header(self, authorization_header:
                                            Optional[str]) -> Optional[str]:
        """
        Extract the Base64 part from the authorization header

        Args:
            authorization_header (Optional[str]): The authorization header

        Returns:
            Optional[str]: The Base64 part of the header or Non
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     Optional[str]) -> (Optional[str],
                                                        Optional[str]):
        """
        Extract user credentials from the decoded Base64 authorization header

        Args:
            decoded_base64_authorization_header (Optional[str]):
            - The decoded Base64 header
        Returns:
            (Optional[str], Optional[str]):
            - A tuple containing the user email and password, or None if fail.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: Optional[str],
                                     user_pwd: Optional[str]) -> Optional[User]
        """
        Returns the User instance based on his email and password

        args:
            user_email (Optional[str]): The user email
            user_pwd (Optional[str]): The user password

        returns:
            Optional[User]: The User instance or None
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> Optional[User]:
        """
        Overloads Auth and retrieves the User instance for a request

        Args:
            request: The Flask request object

        Returns:
            Optional[User]: The User instance or None
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_part = self.extract_base64_authorization_header(auth_header)
        if base64_part is None:
            return None

        decoded = self.decode_base64_authorization_header(base64_part)
        if decoded is None:
            return None

        email, password = self.extract_user_credentials(decoded)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
