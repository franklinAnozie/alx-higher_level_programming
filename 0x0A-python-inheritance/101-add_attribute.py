#!/usr/bin/python3
"""
Module containing function add_attribute
"""


def add_attribute(obj, name, value):
    """add_attribute

    Args:
        obj (object): object to add attribute
        name (string): name of new attribute
        value (object): value of new sttribute

    Raises:
        TypeError: _description_
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    else:
        setattr(obj, name, value)
