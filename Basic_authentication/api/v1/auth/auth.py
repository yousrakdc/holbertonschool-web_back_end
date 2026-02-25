#!/usr/bin/env python3
""" Module of Auth views
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        path_slash = path if path.endswith('/') else path + '/'

        if path_slash in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Authorization header
        """
        if request is None:
            return None

        if request.headers.get('Authorization') is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user
        """
        return None
