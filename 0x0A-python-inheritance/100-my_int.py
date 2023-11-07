#!/usr/bin/python3
"""
Module containing class MyInt
that inherits from class int
"""


class MyInt(int):
    """MyInt
    Rebel childclass of class int
    has == and != operators inverted

    Args:
        int (class): parentclass
    """
    def __eq__(self, name):
        return not (super().__eq__(name))

    def __ne__(self, name):
        return not (super().__ne__(name))
