#!/usr/bin/python3
""" rectangle.py module: contains class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle, inherits from class Base

    Args:
        Base (class): Parent class

    Returns:
        object: rectangle object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init
        Args:
            width (int): width
            height (int): height
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width
        Returns:
            int: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        Args:
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height
        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        Args:
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x
        Returns:
            int: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        Args:
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y
        Returns:
            int:
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        Args:
            value (int): value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area
        Returns:
            int: area
        """
        return self.width * self.height

    def display(self):
        """
        display
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        str
        Returns:
            str: string representation of Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update
        Args:
            *args: variable length argument list
            **kwargs: arbitrary keyword arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        to_dictionary
        Returns:
            dict: dictionary representation of Rectangle
        """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
