#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)
and returns the number of characters written:"""

def write_file(filename="", text=""):
    """Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename (str): name of the file to write to (default: "")
        text (str): text to write to filename (default: "")
    Returns:
        int: number of characters written
    """

    numOfChar = 0
    with open(filename, mode="w", encoding="utf-8") as file:
        numOfChar += file.write(text)

    return numOfChar
