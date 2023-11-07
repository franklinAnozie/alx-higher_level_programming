#!/usr/bin/python3
""" save_to_json_file module """
from json import dump


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function
    Args:
        my_obj: object to be written to file
        filename: file to write to
    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
