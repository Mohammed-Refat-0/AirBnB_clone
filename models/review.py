#!/usr/bin/python3
"""defines the class "Review" """

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class implementation
    Attributes:
    place_id (string): The id of the place
    user_id (string): The id of the user
    tesxt (string): The text of the review"""

    place_id = ''
    user_id = ''
    tesxt = ''
