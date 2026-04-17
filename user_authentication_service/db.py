#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database

        Args:
            email: User's email address
            hashed_password: User's hashed password

        Returns:
            The created User object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database by arbitrary keyword arguments

        Args:
            **kwargs: Arbitrary keyword arguments to filter by

        Returns:
            The first User object matching the filter criteria

        Raises:
            NoResultFound: When no results are found
            InvalidRequestError: When wrong query arguments are passed
        """
        user = self._session.query(User).filter_by(**kwargs).one()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user in the database by user ID

        Args:
            user_id: User ID
            **kwargs: Arbitrary keyword arguments to update

        Raises:
            ValueError: If an argument that
            does not correspond to a user attribute is passed
        """
        user = self.find_user_by(id=user_id)
        valid_columns = User.__table__.columns.keys()
        for key, value in kwargs.items():
            if key not in valid_columns:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
