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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ User object from credentials
        """
        if (user_email is None or type(user_email) is not str or
                user_pwd is None or type(user_pwd) is not str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_auth_header is None:
            return None

        email, password = self.extract_user_credentials(
            decoded_auth_header)
        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)
        return user
