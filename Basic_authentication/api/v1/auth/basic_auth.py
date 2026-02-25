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
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Extract base64 authorization header
        """
        if authorization_header is None or type(authorization_header) != str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

