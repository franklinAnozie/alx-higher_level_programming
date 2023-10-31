#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Function to add two integers or floats and return
    the result as an integer
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: the addition of a and b as an integer or float
        converted to integer if necessary
    Raises:
        TypeError: if a or b are not integers or floats
    """

    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        b = int(b)

    return (a + b)


if __name__ == "__main__":
    add_integer()
