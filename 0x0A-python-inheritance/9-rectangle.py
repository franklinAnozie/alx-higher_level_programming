#!/usr/bin/python3
"""This module contains a class BaseGeometry. This class is the base of all other classes in this project."""


class BaseGeometry:
    def area(self):
        """This method raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates the value argument to be a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """This method instantiates a new Rectangle object with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """This method returns a string representation of the Rectangle object."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """This method returns the area of the Rectangle object."""
        return self.__height * self.__width
