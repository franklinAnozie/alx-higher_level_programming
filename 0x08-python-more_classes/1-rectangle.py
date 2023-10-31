#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle(object):
    """Rectangle class defined by width and height"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the instance if value is an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of the instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the instance if value is an integer >= 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


if __name__ == "__main__":
    Rectangle()
