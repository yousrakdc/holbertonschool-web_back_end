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
