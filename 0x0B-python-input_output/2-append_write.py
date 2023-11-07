#!/usr/bin/python3

def append_write(filename="", text=""):
    """append_write appends a string at the end of a text file
    Args:
        filename (str): name of the file
        text (str): text to append
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
