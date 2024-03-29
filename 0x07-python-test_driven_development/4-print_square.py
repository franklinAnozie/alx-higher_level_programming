#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """Function to print a square with the character #
    in a new line of size size
    Args:
        size (int): size of the square to print
    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and is less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()


if __name__ == "__main__":
    print_square()
