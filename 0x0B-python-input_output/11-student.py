#!/usr/bin/python3
""" students module """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ init method
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json method
        Args:
            attrs: attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
    
    def reload_from_json(self, json):
        """ reload_from_json method
        Args:
            json: json
        """
        for i in json:
            self.__dict__[i] = json[i]
