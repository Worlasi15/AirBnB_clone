#!/usr/bin/python3

"""
Defines the class, City.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents pbject of a City.

    Attributes:
        state_id (str): the city's state ID.
        name (str): City's name.
    """

    def __init__(self, *args, **kwargs):
        """Initialize instance of City"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        sel.name = ""
