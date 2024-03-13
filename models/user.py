#!/usr/bin/python3
"""It defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """ It represents a User.

    Attributes:
        email (str): Email  address of the user.
        password (str): Password of the user.
        first_name (str): Firstname of the user.
        last_name (str): Lastname of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
