#!/usr/bin/python3

"""
Defines the class, State.
"""

from models.base_model import
BaseModel


class State(BaseModel):
    """Represents an instance of the class
    State (object)

    Attributes:
    name (str):state's name.
    """

    def init(self, *args, **kwargs):
        """Initialize State instance,"""
        super().init(*args, **kwargs)
        self.name = ""
