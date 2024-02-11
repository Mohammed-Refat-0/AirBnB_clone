#!/usr/bin/python3
"""defines the class "City" """

from models.base_model import BaseModel


class City(BaseModel):
    """City class implementation
    Attributes:
    name (string): The name of the city
    state_id (string): The id of the state"""

    state_id = ''
    name = ''
