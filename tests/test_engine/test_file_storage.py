#!/usr/bin/python3
"""Test module for FileStorage class"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for test cases"""
        # Create a test instance for each class
        cls.user = User()
        cls.state = State()
        cls.city = City()
        cls.place = Place()
        cls.amenity = Amenity()
        cls.review = Review()

    @classmethod
    def tearDownClass(cls):
        """Clean up after test cases"""
        del cls.user
        del cls.state
        del cls.city
        del cls.place
        del cls.amenity
        del cls.review

    def test_all_method(self):
        """Test the all() method"""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        """Test the new() method"""
        # Ensure that new objects are added to storage
        user_id = self.user.id
        state_id = self.state.id
        city_id = self.city.id
        place_id = self.place.id
        amenity_id = self.amenity.id
        review_id = self.review.id

        self.assertTrue(f"User.{user_id}" in storage.all())
        self.assertTrue(f"State.{state_id}" in storage.all())
        self.assertTrue(f"City.{city_id}" in storage.all())
        self.assertTrue(f"Place.{place_id}" in storage.all())
        self.assertTrue(f"Amenity.{amenity_id}" in storage.all())
        self.assertTrue(f"Review.{review_id}" in storage.all())

    def test_save_method(self):
        """Test the save() method"""
        # Create a new object, save it, and check if it's in the JSON file
        new_user = User()
        new_user.first_name = "John"
        new_user.last_name = "Doe"
        new_user.email = "johndoe@example.com"
        new_user.password = "password123"

        user_id = new_user.id
        storage.save()

        with open("file.json", "r", encoding="utf-8") as file:
            data = file.read()
            self.assertTrue(user_id in data)

    def test_reload_method(self):
        """Test the reload() method"""
        # Create a new object, save it, reload, and check if it's accessible
        new_state = State()
        new_state.name = "California"
        state_id = new_state.id
        storage.save()
        storage.reload()

        all_objs = storage.all()
        self.assertTrue(f"State.{state_id}" in all_objs)

    @classmethod
    def tearDown(cls):
        """Clean up temporary files"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    unittest.main()
