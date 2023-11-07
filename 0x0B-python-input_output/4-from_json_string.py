#!/usr/bin/python3
"""Module for from_json_string method"""
from json import loads


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string
    Args:
        my_str: string to be converted to object
    Returns:
        object represented by JSON string
    """
    return loads(my_str)
