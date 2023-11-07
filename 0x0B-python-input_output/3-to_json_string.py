#!/usr/bin/python3
"""Module for to_json_string method"""
from json import dumps

def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: object to be converted to JSON
    Returns:
        JSON representation of the object
    """
    return dumps(my_obj)
