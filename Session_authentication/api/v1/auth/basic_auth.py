#!/usr/bin/env python3
"""
Basic Authentication module for the API.

This module provides the base Auth class that handles authentication
for the API endpoints.
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    '''Basic Auth inherit form Auth'''

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''Extract and return a Base64 part of
        Authorization header for a basic auth'''

        if (authorization_header is None
            or not isinstance(authorization_header, str)
                or not authorization_header.startswith('Basic ')):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        '''Returning the decoded value of a Base64 string'''

        if (base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            b64decode = base64.b64decode(base64_authorization_header)
            utf8decode = b64decode.decode('utf-8')
            return utf8decode

        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        '''Extract user credentials method'''
        if (decoded_base64_authorization_header is None
                or not isinstance(decoded_base64_authorization_header, str)):
            return None, None
        elif ':' not in decoded_base64_authorization_header:
            return None, None

        email = decoded_base64_authorization_header.split(':')[0]
        password = decoded_base64_authorization_header.split(':')[1]

        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''Return user credentila as an object'''

        if (user_email is None or not isinstance(user_email, str)
                or user_pwd is None or not isinstance(user_pwd, str)):
            return None

        user = User.search({"email": user_email})
        if not user:
            return None

        for cred in user:
            if cred and cred.is_valid_password(user_pwd):
                return cred

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user method'''
        if request:
            authorization = self.authorization_header(request)
            base64 = self.extract_base64_authorization_header(authorization)
            decodeBase64 = self.decode_base64_authorization_header(base64)
            (email, password) = self.extract_user_credentials(decodeBase64)
            user = self.user_object_from_credentials(email, password)

            return user
        return None
