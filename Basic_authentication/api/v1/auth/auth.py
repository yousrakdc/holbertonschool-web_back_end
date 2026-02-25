#!/usr/bin/env python3
from typing import List, TypeVar
from flask import request

"""Auth class for handling authentication methods
"""
class Auth:
	"""Auth class for handling authentication methods"""
	def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
		"""Returns False. path and excluded_paths will be used later."""
		return False

	def authorization_header(self, request=None) -> str:
		"""Returns None. request will be the Flask request object."""
		return None

	def current_user(self, request=None) -> TypeVar('User'):
		"""Returns None. request will be the Flask request object."""
		return None

