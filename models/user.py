#!/usr/bin/python3
"""
Defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): Email of the user
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
