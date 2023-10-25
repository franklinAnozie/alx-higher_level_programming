#!/usr/bin/python3
"""Define a class Square that defines a square by: (based on 2-square.py)"""


class Square(object):
    """ This square class has a private instance attribute: size"""
    def __init__(self, size=0):
        """ Initialize a new Square.
        Args:
            size (int): The size of the new Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return the area of the Square """
        return self.__size * self.__size
