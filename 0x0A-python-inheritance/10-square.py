#!/usr/bin/python3
"""This module contains a class BaseGeometry.
This class is the base of all other classes in this project."""


class BaseGeometry:
    """This class is the base of all other classes in this project."""

    def area(self):
        """This method raises an Exception with
        the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value argument
        to be a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ instantiates a new Rectangle object with width and height. """
    def __init__(self, width, height):
        """ instantiates a new Rectangle object with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ returns a string representation of the Rectangle object."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """ returns the area of the Rectangle object."""
        return self.__height * self.__width


class Square(Rectangle):
    """ instantiates a new Square object with size."""
    def __init__(self, size):
        """ instantiates a new Square object with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
