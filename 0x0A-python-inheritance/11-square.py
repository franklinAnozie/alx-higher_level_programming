#!/usr/bin/python3
"""
Module containing class Square
that inherits from class Rectangle
in module (9-rectangle.py)
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square
    Inherits from class Rectangle

    Args:
        Rectangle (Class): Parent class
    """
    def __init__(self, size):
        """__init__
        Class Rectangle constructor

        Args:
            size (int): size of Square object
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area
        returns area of Square object

        Returns:
            int: area of self
        """
        return (self.__size ** 2)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
