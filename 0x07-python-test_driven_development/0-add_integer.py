#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
        a = int(a)
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
        b = int(b)

    return (a + b)


if __name__ == "__main__":
    add_integer()
