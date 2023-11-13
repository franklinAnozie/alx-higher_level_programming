#!/usr/bin/python3
"""
Module containing Square class that inherites from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square
    Class Square that inherits from Rectangle

    Args:
        Rectangle (Class): Super class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__
        Constructor for class Square

        Args:
            size (int): size of square
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """__str__
        String representation of Square object

        Returns:
            string: representation of Square object
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}")

    @property
    def size(self):
        """size getter

        Returns:
            int: size of square object
        """
        return self.__size

    @size.setter
    def size(self, size):
        """size setter

        Args:
            size (int): new size value
        """
        self.width = size
        self.height = self.width
        self.__size = self.width

    def update(self, *args, **kwargs):
        """update
        update attributes of a square object
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
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
        """to_dictionary
        genereates representation of a square as dict

        Returns:
            dict: representation of a square object
        """
        new_dict = dict()
        new_dict.update({"id": self.id})
        new_dict.update({"size": self.size})
        new_dict.update({"x": self.x})
        new_dict.update({"y": self.y})
        return new_dict
