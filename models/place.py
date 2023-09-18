#!/usr/bin/python3

"""
Defines the class, Place.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents an instance of the Place class(object).

    Attributes:
        city_id (str): The place's City ID
        user_id (str): The place's User ID
        name (str): The place's name
        description (str): The place's description
        number_rooms (int): The number of rooms in the place
        number_bathrooms (int): The place's number of bathrooms
        max_guest (int): The number of guests the place can hold
        price_by_night (int): The place's price by night
        latitude (float): The place's latitude
        longitude (float): The place's longitude
        amenity_ids (list): The place's amenity IDs
    """

    def __init__(self, *args, **kwargs):
        """Initialize Placeinstance"""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
