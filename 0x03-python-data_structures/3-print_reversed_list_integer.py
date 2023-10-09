#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = []
    length = len(my_list) - 1
    while length >= 0:
        new_list.append(my_list[length])
        length -= 1
    for i in new_list:
        print("{:d}".format(i))


if __name__ == "__main__":
    print_reversed_list_integer()
