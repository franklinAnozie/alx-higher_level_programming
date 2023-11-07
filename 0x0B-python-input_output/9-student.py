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

    def to_json(self):
        """ to json method
        Return:
            json representation of self
        """
        return vars(self)
