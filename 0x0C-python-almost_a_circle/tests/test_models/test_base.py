#!/usr/bin//python3
"""
Module containing test for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase
    Unittestfor class Base

    Args:
        unittest (class): unittest
    """
    def test_base_constructor(self):
        """test_base_constructor
        test the Base class constructor without id
        """
        obj = Base()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)

    def test_base_constructor_with_id(self):
        """test_base_constructor_with_id
        tests the Base class constructor with id args
        """
        obj = Base(42)
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 42)

    def test_base_to_json_string(self):
        new_dict = {'x': 2, 'y': 8, 'id': 1}
        output = Base.to_json_string([new_dict])
        self.assertEqual(output, '[{"x": 2, "y": 8, "id": 1}]')

        output = Base.to_json_string(None)
        self.assertEqual(output, "[]")

        output = Base.to_json_string()
        self.assertEqual(output, "[]")

        output = Base.to_json_string([])
        self.assertEqual(output, "[]")


if __name__ == '__main__':
    unittest.main()
