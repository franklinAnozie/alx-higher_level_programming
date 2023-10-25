#!/usr/bin/python3
"""Define a class Square that defines a square by: (based on 3-square.py)"""


class Square(object):
    """ This square class has private instance attributes: size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            position (tuple): The position of the new Square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not isinstance(value[0], int) or not isinstance(value[1], int):
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Return the area of the Square """
        return self.__size * self.__size

    def my_print(self):
        """ Print the square with the character # """
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print("", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
