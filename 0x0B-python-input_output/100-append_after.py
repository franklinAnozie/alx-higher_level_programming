#!/usr/bin/python3
""" Module that contains the function append_after """


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file, after each line containing a
    specific string
    Args:
        filename (str): name of the file
        search_string (str): string to search
        new_string (str): string to append

    Returns:
        None
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        f.seek(0)
        f.writelines(new_lines)
