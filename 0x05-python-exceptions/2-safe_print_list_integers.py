#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    retVal = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            retVal += 1
        except (TypeError, ValueError):
            continue
    print()
    return retVal


if __name__ == "__main__":
    safe_print_list_integers()
