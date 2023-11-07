#!/usr/bin/python3
""" load_from_json_file """
from json import load


def load_from_json_file(filename):
    """ load_from_json_file
    Args:
        filename (str): name of the file to read from
    Returns:
        object: object represented by a JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return load(file)
