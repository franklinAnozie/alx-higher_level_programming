#!/usr/bin/python3

def print_square(size):
    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(int(size)):
        for j in range(int(size)):
            print("#", end="")
        print()
