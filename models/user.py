#!/usr/bin/python3
"""defines the class "User" """
from models.base_model import BaseModel
import datetime
import uuid


class User(BaseModel):
    """User class implementation
    Attributes:
    id (string): The id of the user
    email (string): The email of the user
    password (string): The password of the user"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
