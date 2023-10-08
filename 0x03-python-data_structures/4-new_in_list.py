#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            new_list.append(element)
            continue
        new_list.append(my_list[i])

    return new_list


if __name__ == "__main__":
    new_in_list()
