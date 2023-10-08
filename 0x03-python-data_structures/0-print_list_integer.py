#!/usr/bin/python3
# function that prints all integers of a list.
def print_list_integer(my_list=[]):
    for i in my_list:
        print(f"{i}", end="")
    
    print("")

print_list_integer([1, 2, 3, 4, 5])
