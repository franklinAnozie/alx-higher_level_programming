#!/usr/bin/python3
""" square.py module: contains class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        init
        Args:
            size (int): size
            x (int): x
            y (int): y
            id (int): id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str
        Returns:
            str: string representation of Square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size
        Returns:
            int: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        Args:
            value (int): value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update
        Args:
            *args: arguments
            **kwargs: keyword arguments
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        to_dictionary
        Returns:
            dict: dictionary representation of Square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
