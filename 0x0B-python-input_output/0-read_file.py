#!/usr/bin/python3
"""Read a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdout
    Args:
        filename (str): name of the file to read from (default: "")

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
