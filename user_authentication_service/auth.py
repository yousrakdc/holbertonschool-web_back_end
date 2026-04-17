#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt

    Args:
        password: Password string to hash

    Returns:
        Bytes representation of the salted hash
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generate a new UUID

    Returns:
        String representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            email: User's email address
            password: User's password

        Returns:
            The created User object

        Raises:
            ValueError: If a user with the email already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password).decode('utf-8')
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials

        Args:
            email: User's email address
            password: User's password

        Returns:
            True if credentials are valid, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password.encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user

        Args:
            email: User's email address

        Returns:
            Session ID as a string, or None if user not found
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get user from session ID

        Args:
            session_id: Session ID string

        Returns:
            User object if found, None otherwise
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session

        Args:
            user_id: User ID integer
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for a user

        Args:
            email: User's email address

        Returns:
            Reset password token as a string

        Raises:
            ValueError: If user with the email does not exist
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """Update a user's password using reset token

        Args:
            reset_token: Reset token string
            password: New password string

        Raises:
            ValueError: If user with the reset token does not exist
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password).decode('utf-8')
            self._db.update_user(
                user.id, hashed_password=hashed_password, reset_token=None)
        except NoResultFound:
            raise ValueError
