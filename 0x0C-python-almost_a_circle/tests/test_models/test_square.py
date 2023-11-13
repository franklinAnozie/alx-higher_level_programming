"""
Module containing unittests for Square class
"""
import io
import unittest
from models.square import Square
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """TestSquare
    Test case class for Square

    Args:
        unittest (Class): Unittest
    """

    def test_square_constructor(self):
        """test_square_constructor
        tests that the Square class basic constructor works
        """
        sqr = Square(10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)

    def test_square_constructor_with_id(self):
        """test_square_constructor_with_id
        Test that the full args passed to the constructor are functional
        """
        sqr = Square(5, 1, 1, 10)
        self.assertEqual(sqr.height, 5)
        self.assertEqual(sqr.width, 5)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 1)
        self.assertEqual(sqr.id, 10)

    def test_square_setters(self):
        """test_square_setters
        test property setters of class square
        """
        sqr = Square(10)
        self.assertEqual(sqr.width, 10)
        sqr.width = 30
        sqr.x = 5
        sqr.y = 10
        self.assertEqual(sqr.width, 30)
        sqr.size = 20
        self.assertEqual(sqr.width, 20)
        self.assertEqual(sqr.height, 20)
        self.assertEqual(sqr.size, 20)
        self.assertEqual(sqr.x, 5)
        self.assertEqual(sqr.y, 10)

    def test_square_set_size_error(self):
        """test_square_set_size_error
        test that setting size with invalid value raises
        expected error
        """
        sqr = Square(5)
        with self.assertRaises(ValueError):
            sqr.size = -2
        with self.assertRaises(TypeError):
            sqr.size = "invalid"

    def test_sqaure_str(self):
        """test_sqaure_str
        tests the string representation of square
        """
        sqr = Square(30, 0, 0, 12)
        self.assertEqual(str(sqr), "[Square] (12) 0/0 - 30")
        sqr.size = 10
        sqr.x = 2
        sqr.y = 2
        self.assertEqual(str(sqr), "[Square] (12) 2/2 - 10")

    def test_square_update_args(self):
        sqr = Square(10)
        self.assertEqual(sqr.size, 10)
        sqr.update(10, 5, 1, 1)
        self.assertEqual(sqr.size, 5)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 1)
        self.assertEqual(sqr.id, 10)

    def test_square_update_kwargs(self):
        sqr = Square(1)
        sqr.update(id=10, size=10, x=1, y=4)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 1)
        self.assertEqual(sqr.y, 4)
        self.assertEqual(sqr.id, 10)

    def test_square_to_dictionary(self):
        """test_recangle_to_dicttionary
        test to dictionary method of rectangle
        """
        sqr = Square(5, 1, 1, 10)
        output = str((sqr.to_dictionary()))
        # Verify that the displayed rectangle matches the expected output
        test2 = "{'id': 10, 'size': 5, 'x': 1, 'y': 1}"
        self.assertEqual(output, test2)
