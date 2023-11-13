"""
Module containing unittests for rectangle class
"""
import io
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """TestRectangle
    Unittest for class rectangle

    Args:
        unittest (class): unittest
    """
    def setUp(self):
        # Create a rectangle object for testing
        self.r1 = Rectangle(3, 2, 0, 0, 34)

    def test_rectangle_constructor(self):
        """test_rectangle_constructor
        test the Rectangle class constructor without id
        """
        rect = Rectangle(10, 20)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_rectangle_constructor_with_id(self):
        """test_rectangle_constructor_with_id
        tests the rectangle class with id
        """
        rect = Rectangle(10, 20, id=42)
        self.assertIsInstance(rect, Rectangle)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 42)

    def test_rectangle_setters(self):
        """test_rectangle_setters
        test property setters of class Rectangle
        """
        rect = Rectangle(10, 20)
        rect.width = 30
        rect.height = 40
        rect.x = 5
        rect.y = 10
        self.assertEqual(rect.width, 30)
        self.assertEqual(rect.height, 40)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 10)

    def test_width_getter(self):
        """test_width_getter
        """
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)

    def test_width_setter(self):
        """test_width_setter
        """
        r = Rectangle(10, 20)
        r.width = 30
        self.assertEqual(r.width, 30)

    def test_width_setter_type_error(self):
        """test_width_setter_type_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_height_setter_type_error(self):
        """test_height_setter_type_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_x_setter_type_error(self):
        """test_x_setter_type_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.x = "invalid"

    def test_y_setter_type_error(self):
        """test_y_setter_type_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test_width_setter_value_error(self):
        """test_width_setter_value_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter_value_error(self):
        """test_height_setter_value_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.height = -1

    def test_x_setter_value_error(self):
        """test_x_setter_value_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_setter_value_error(self):
        """test_y_setter_value_error
        """
        r = Rectangle(10, 20)
        with self.assertRaises(ValueError):
            r.y = -2

    def test_area(self):
        """test_area
        """
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """test_display
        """
        # Redirect stdout to capture the printed output
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.r1.display()

            # Get the captured output
            output = mock_stdout.getvalue()

        # Verify that the displayed rectangle matches the expected output
        expected_output = "###\n###\n"
        self.assertEqual(output, expected_output)

    def test_str(self):
        """test_str
        """
        r1 = Rectangle(3, 2, 0, 0, 34)
        expected_output = "[Rectangle] (34) 0/0 - 3/2"
        self.assertEqual(str(r1), expected_output)

    def test_update_args(self):
        """test_update_args
        """
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        rect.update(30, 40, 5, 10, 60)
        self.assertEqual(rect.width, 40)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 60)
        self.assertEqual(rect.id, 30)

    def test_update_kwargs(self):
        """test_update_kwargs
        """
        rect2 = Rectangle(1, 2)
        rect2.update(id=30, width=40, height=5, x=10, y=60)
        self.assertEqual(rect2.width, 40)
        self.assertEqual(rect2.height, 5)
        self.assertEqual(rect2.x, 10)
        self.assertEqual(rect2.y, 60)
        self.assertEqual(rect2.id, 30)

    def test_recangle_to_dicttionary(self):
        """test_recangle_to_dicttionary
        test to dictionary method of rectangle
        """
        r1 = Rectangle(10, 2, 1, 9, 1)
        r1_dictionary = r1.to_dictionary()
        output = str(r1_dictionary)
        # Verify that the displayed rectangle matches the expected output
        test2 = "{'width': 10, 'height': 2, 'x': 1, 'y': 9, 'id': 1}"
        self.assertEqual(output, test2)


if __name__ == '__main__':
    unittest.main()
