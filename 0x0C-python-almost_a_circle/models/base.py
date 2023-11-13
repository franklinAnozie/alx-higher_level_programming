#!/usr/bin/python3
from json import dumps, loads

class Base(object):

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", "r", "utf-8") as f:
                return [cls.create(**obj) for obj in cls.from_json_string(f.read())]
        except:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".csv", "w") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(cls.__name__ + ".csv", "r", "utf-8") as f:
                return [cls.create(**obj) for obj in cls.from_json_string(f.read())]
        except:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
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
  