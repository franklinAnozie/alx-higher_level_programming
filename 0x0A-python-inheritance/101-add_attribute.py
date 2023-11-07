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
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
