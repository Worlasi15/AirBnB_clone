#!/usr/bin/python3

"""
Define the User class.
"""

from models.base_model import
BaseModel


class User(BaseModel):
    """Represents a User object.

    Attributes:
    email(str):user's email address.
    password(str):user's password.
    first_name(str):user's first name.
    last_name(str):user's last name.
    """

    def init(self, *args, **kwargs):
        """initialize User instance."""
        super()._ _init_ _(*args, **kwargs):
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
