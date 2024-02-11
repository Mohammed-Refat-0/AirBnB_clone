#!/usr/bin/python3
"""defines the class "Place" """

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class implementation
    Attributes:
    city_id (string): The id of the city
    user_id (string): The id of the user
    name (string): The name of the place
    description (string): The description of the place
    number_rooms (int): The number of rooms
    number_bathrooms (int): The number of bathrooms
    max_guest (int): The maximum number of guests
    price_by_night (int): The price per night
    latitude (float): The latitude of the place
    longitude (float): The longitude of the place
    amenity_ids (list): The list of amenities"""

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
