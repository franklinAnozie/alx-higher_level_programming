#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b >= 0:
        for i in range(b):
            c = c * a
        return (c)
    else:
        b = b * -1
        for i in range(b):
            c = c * a
        c = 1 / c
        return (c)
