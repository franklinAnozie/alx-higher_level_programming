#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    counter = 0
    for char in str:
        if counter != n:
            new_str += char
        counter += 1
    return (new_str)
