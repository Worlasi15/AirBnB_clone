#!/usr/bin/python3
"""Test module for Amenity class"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertIsInstance(amenity.name, str)
        self.assertEqual(amenity.name, "")

    def test_attribute_types(self):
        """Test the types of Amenity attributes"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_attribute_inheritance(self):
        """Test that Amenity inherits attributes from BaseModel"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))

    def test_str_representation(self):
        """Test the string representation of Amenity"""
        amenity = Amenity()
        amenity.name = "WiFi"
        str_repr = str(amenity)
        self.assertEqual(str_repr, "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__))

    def test_to_dict_method(self):
        """Test the to_dict() method of Amenity"""
        amenity = Amenity()
        amenity.name = "Pool"
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Pool')


if __name__ == "__main__":
    unittest.main()
