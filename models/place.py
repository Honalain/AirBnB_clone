#!/usr/bin/python3
"""
Module for Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from BaseModel class

     Attributes:
        city_id (str): id of the city
        user_id (str): id of the user
        name (str): name of the place.
        description (str): description of the place to stay
        number_rooms (int): number of rooms of
        the place to be booked
        number_bathrooms (int): number of bathrooms of
        the place found in the room

        max_guest (int): maximum number of guests of
        the place can occupy that place

        price_by_night (int): price by night of
        the place to choosen place
        latitude (float): latitude of the place
        longitude (float): longitude of the place
        amenity_ids (list): list of Amenity ids of the class

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
