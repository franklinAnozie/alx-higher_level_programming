#!/usr/bin/python3
"""Module to print a name"""


def say_my_name(first_name, last_name=""):
    """Function to print a name in a new line with the format:
    My name is <first name> <last name>
    Args:
        first_name (str): first name (required)
        last_name (str): last name (optional)
    Raises:
        TypeError: if first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    say_my_name()
