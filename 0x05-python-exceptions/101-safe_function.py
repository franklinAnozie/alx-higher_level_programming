#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None


if __name__ == "__main__":
    safe_function()
