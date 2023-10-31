#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(f"{text[i]}")
            print()
        elif text[i] == " " and (text[i-1] == "." or text[i-1] == "?" or text[i-1] == ":"):
            while text[i] == " ":
                i += 1
            print(f"{text[i]}", end="")
        else:
            print(f"{text[i]}", end="")
        i += 1
