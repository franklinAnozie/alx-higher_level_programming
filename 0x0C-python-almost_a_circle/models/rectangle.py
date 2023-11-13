#!/usr/bin/python3
"""
Module containing class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle
    Class rectangle, inherits from class Base

    Args:
        Base (class): Parent class

    Returns:
        object: rectangle object
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__
        Constructor

        Args:
            width (int): width
            height (int): height
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): precise id for object. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width
        getter for width

        Returns:
            int: value for width
        """
        return self.__width

    @property
    def height(self):
        """height
        getter for height

        Returns:
            int: value of height
        """
        return self.__height

    @property
    def x(self):
        """x
        getter for x

        Returns:
            int: value of x
        """
        return self.__x

    @property
    def y(self):
        """y
        getter for y

        Returns:
            int: value of y
        """
        return self.__y

    def area(self):
        """area
        returns area of rectangle object

        Returns:
            int: area of object
        """
        return (self.__height * self.__width)

    @width.setter
    def width(self, width):
        """width
        sets value of width

        Args:
            width (int): new value for width

        Raises:
            TypeError: when width is not a integer
            ValueError: when width is less or equal to 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 1:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height
        sets value of height

        Args:
            height (int): new value for height

        Raises:
            TypeError: when height is not a integer
            ValueError: when height is less or equal to 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 1:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        """x
        sets the value of x

        Args:
            x (int): new value for x

        Raises:
            TypeError: when x is not a integer
            ValueError: when x is less than 0
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        """y
        sets the value of y

        Args:
            y (int): new value for y

        Raises:
            TypeError: when y is not a integer
            ValueError: when y is less than 0
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def display(self):
        """display
        display rectangle object
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """__str__
        string representation of rectangle object

        Returns:
            string: representation of Rectangle object
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """update
        update attributes of a rectangle object
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key in ("height", "width", "x", "y"):
                    tmp = "_" + self.__class__.__name__ + "__" + key
                    self.__dict__.update({tmp: value})
                elif key == "id":
                    self.__dict__.update({key: value})

    def to_dictionary(self):
        """to_dictionary
        genereates representation of a Rectangle as dict

        Returns:
            dict: representation of a Rectangle object
        """
        new_dict = dict()
        new_dict.update({"width": self.width})
        new_dict.update({"height": self.height})
        new_dict.update({"x": self.x})
        new_dict.update({"y": self.y})
        new_dict.update({"id": self.id})
        return new_dict
