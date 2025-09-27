#!/usr/bin/env python3
"""
Basic authentication module
"""

import base64
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
