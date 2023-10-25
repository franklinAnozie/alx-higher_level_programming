#!/usr/bin/python3
"""Define a class Square that defines a square by: (based on 4-square.py)"""


class Square(object):
    """ This square class has a private instance attribute: size"""
    def __init__(self, size):
        """ Initialize a new Square.
        Args:
            size (int): The size of the new Square.
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the area of the Square """
        return self.__size * self.__size

    def my_print(self):
        """ Print the square with the character # """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
