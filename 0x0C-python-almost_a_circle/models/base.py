#!/usr/bin/python3
"""
Module containing class Base
"""
import json


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__
        Base object constructor

        Args:
            id (int, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries=None):
        """to_json_string

        Args:
            list_dictionaries (list, optional): list of dictionary.
            Defaults to None.

        Returns:
            json string: json string representation of list_dictionaries
        """
        if list_dictionaries is not None and len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs=None):
        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            pass
