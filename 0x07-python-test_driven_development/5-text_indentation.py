#!/usr/bin/python3
"""Module to print a text with 2 new lines after each
of these characters: ., ? and :"""


def text_indentation(text):
    """Function to print a text with 2 new lines after each
    of these characters: ., ? and :
    Args:
        text (str): text to print with 2 new lines after each
        of these characters: ., ? and :
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(f"{text[i]}")
            print()
        elif text[i] == " " and (text[i-1] == "."
                                 or text[i-1] == "?" or text[i-1] == ":"):
            while text[i] == " ":
                i += 1
            print(f"{text[i]}", end="")
        else:
            print(f"{text[i]}", end="")
        i += 1


if __name__ == "__main__":
    text_indentation()
