#!/usr/bin/python3
from json import dumps, loads

class Base(object):
    """
    Class Base

    Returns:
        object: shape object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__
        Base object constructor

        Args:
            id (int, optional): _description_. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string

        Args:
            list_dictionaries (list, optional): list of dictionary.
            Defaults to None.

        Returns:
            json string: json string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Args:
            list_objs (list, optional): list of objects. Defaults to None.
        """
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
    
    @staticmethod
    def from_json_string(json_string):
        """from_json_string

        Args:
            json_string (json string): json string

        Returns:
            list: list of json string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """create

        Returns:
            object: object with all attributes already set

        Args:
            **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """load_from_file

        Returns:
            list: list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r", "utf-8") as f:
                return [cls.create(**obj) for obj in cls.from_json_string(f.read())]
        except:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv

        Args:
            list_objs (list, optional): list of objects. Defaults to None.
        """
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".csv", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv

        Returns:
            list: list of instances
        """
        try:
            with open(cls.__name__ + ".csv", "r", "utf-8") as f:
                return [cls.create(**obj) for obj in cls.from_json_string(f.read())]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw

        Args:
            list_rectangles (list): list of rectangles
            list_squares (list): list of squares
        """
        import turtle
        from random import randint

        turtle.title("My first turtle")
        turtle.setup(width=800, height=600)
        turtle.bgcolor("black")
        turtle.hideturtle()
        turtle.speed(0)

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(randint(-400, 400), randint(-300, 300))
            turtle.pendown()
            turtle.color("white")
            turtle.pensize(3)
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.right(90)
                turtle.forward(rectangle.height)
                turtle.right(90)
        
        for square in list_squares:
            turtle.penup()
            turtle.goto(randint(-400, 400), randint(-300, 300))
            turtle.pendown()
            turtle.color("white")
            turtle.pensize(3)
            for i in range(4):
                turtle.forward(square.size)
                turtle.right(90)
        
        turtle.done()
  