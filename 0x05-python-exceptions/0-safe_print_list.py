#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    retVal = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            retVal += 1
        print()
    except IndexError:
        print()
    return (retVal)


if __name__ == "__main__":
    safe_print_list()
