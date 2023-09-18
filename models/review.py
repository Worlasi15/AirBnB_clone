#!usr/bin/python3

"""
Define the Review class.
"""

from models.base_model import
BaseModel


class Review(BaseModel):
    """Represents a Review object.

    Attributes:
    place_id(str):The review's Place ID
    user_id(str):The review;'s User ID
    text(str):The review's text content
    """

    def init(self, *args, **kwargs):
        """Iniitialize Review instance."""
        super().init(*args, **kwargs)
        self.place_id = ""
        self.use_id = ""
        self.text + ""
