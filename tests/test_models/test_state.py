#!/usr/bin/python3

import unittest
from models.state import State
from time import sleep
import models
import os
import datetime import datetime


class TestState(unittest.TestCase):
    def test_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_inheritance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
