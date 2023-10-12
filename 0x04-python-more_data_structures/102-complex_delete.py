#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    for keys, values in a_dictionary.items():
        if values == value:
            del_list.append(keys)
    for key in del_list:
        del a_dictionary[key]
    return a_dictionary
