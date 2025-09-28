#!/usr/bin/env python3
"""
User module
"""

from flask import jsonify, abort, request
import hashlib
from models.base import Base
app_views = __import__('api.v1.views').app_views

class User(Base):
    """
    User class that inherits from Base

    Attributes:
        email (str): The email of the user
        _password (str): The hashed password of the user
        first_name (str): The first name of the user
        last_name (str): The last name of the user
    """

    def __init__(self, *args: list, **kwargs: dict):
        """ Initialize a User instance
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email')
        self._password = kwargs.get('_password')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')

    @property
    def password(self) -> str:
        """ Getter of the password
        """
        return self._password

    @password.setter
    def password(self, pwd: str):
        """
        Setter of a new password: encrypt in SHA256

        Args:
            pwd (str): The new password
        Returns: None
        """
        if pwd is None or type(pwd) is not str:
            self._password = None
        else:
            self._password = hashlib.sha256(pwd.encode()).hexdigest().lower()

    def is_valid_password(self, pwd: str) -> bool:
        """
        Validate a password

        Args:
            pwd (str): The password to validate
        Returns:
            bool: True if the password is valid, False otherwise
        """
        if pwd is None or type(pwd) is not str:
            return False
        if self.password is None:
            return False
        pwd_e = pwd.encode()
        return hashlib.sha256(pwd_e).hexdigest().lower() == self.password

    def display_name(self) -> str:
        """
        Display User name based on email/first_name/last_name

        Returns:
            str: Formatted name or empty string if no name/email
        """
        if self.email is None and self.first_name is None \
                and self.last_name is None:
            return ""
        if self.first_name is None and self.last_name is None:
            return "{}".format(self.email)
        if self.last_name is None:
            return "{}".format(self.first_name)
        if self.first_name is None:
            return "{}".format(self.last_name)
        else:
            return "{} {}".format(self.first_name, self.last_name)

    @app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
    def get_user(user_id):
        """
        Retrieve a User object by id or 'me'
        """
        if user_id == 'me':
            user = getattr(request, 'current_user', None)
            if user is None:
                abort(404)
            return jsonify(user.to_dict()), 200

        user = User.get(user_id)
        if user is None:
            abort(404)
        return jsonify(user.to_dict()), 200
