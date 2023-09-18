#!/usr/bin/python3
"""Test module for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_instance_creation(self):
        """Test instance creation"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_id_creation(self):
        """Test ID creation"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertIsInstance(base_model.id, str)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of BaseModel"""
        base_model = BaseModel()
        str_repr = str(base_model)
        self.assertEqual(str_repr, "[BaseModel] ({}) {}".format(
            base_model.id, base_model.__dict__))

    def test_save_method(self):
        """Test the save method"""
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'],
                         base_model.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test initialization with kwargs"""
        kwargs = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-02-01T00:00:00.000000',
            'name': 'Test'
        }
        base_model = BaseModel(**kwargs)

        self.assertEqual(base_model.id, kwargs['id'])
        self.assertEqual(base_model.name, kwargs['name'])
        self.assertEqual(base_model.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(base_model.updated_at.isoformat(),
                         kwargs['updated_at'])

    def test_kwargs_unknown_attributes(self):
        """Test initialization with unknown attributes in kwargs"""
        kwargs = {
            'id': '123',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-02-01T00:00:00.000000',
            'unknown_attr': 'Unknown'
        }
        base_model = BaseModel(**kwargs)

        self.assertEqual(base_model.id, kwargs['id'])
        self.assertTrue(hasattr(base_model, 'unknown_attr'))
        self.assertEqual(getattr(base_model, 'unknown_attr'),
                         kwargs['unknown_attr'])

    def test_kwargs_empty_dict(self):
        """Test initialization with an empty dictionary as kwargs"""
        kwargs = {}
        base_model = BaseModel(**kwargs)

        self.assertIsInstance(base_model, BaseModel)

    def test_kwargs_none(self):
        """Test initialization with None as kwargs"""
        base_model = BaseModel(**None)

        self.assertIsInstance(base_model, BaseModel)


if __name__ == "__main__":
    unittest.main()
