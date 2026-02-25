#!/usr/bin/env python3
"""
Basic authentication module
"""

import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


"""BasicAuth class"""


class BasicAuth(Auth):
    """ BasicAuth class
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Extract base64 authorization header
        """
        if (authorization_header is None or
                type(authorization_header) is not str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode base64 authorization header
        """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None

        try:
            decoded_bytes = base64.b64decode(
                base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials
        """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password
