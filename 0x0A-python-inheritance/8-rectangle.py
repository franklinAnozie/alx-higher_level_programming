#!/usr/bin/python3
"""
Module containing Class Rectangle that inherits from
Class BaseGeometry in module "7-base_geometry.py"
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle
    inherits from class BaseGeometry

    Args:
        BaseGeometry (class): Base class for class Rectangle
    """
    def __init__(self, width, height):
        """__init__
        constructor for class Rectangle

        Args:
            width (int): width of rectangle object to be created
            height (int): height of rectangle object to be created
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
