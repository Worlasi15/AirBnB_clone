#!/usr/bin/python3

"""
Defines Amenity class
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Representing Amenity object

    Attributes:
        name (str): name of amenity
    """

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = ""

