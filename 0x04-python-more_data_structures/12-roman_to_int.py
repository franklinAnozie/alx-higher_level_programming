#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_number = 0
    prev = ""
    my_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    if roman_string is not None and isinstance(roman_string, str):
        for i in roman_string:
            if i in my_dict:
                if prev != "":
                    if my_dict[prev] < my_dict[i]:
                        roman_number = roman_number - (2 * my_dict
                                                       [prev]) + my_dict[i]
                    else:
                        roman_number += my_dict[i]
                else:
                    roman_number += my_dict[i]
                prev = i

    return roman_number
