#!/usr/bin/python3
"""This module contains a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly)
from the specified class ; otherwise False."""


def inherits_from(obj, a_class):
    """inherits_from
    checks that obj and a_class are same or share the same superclasss

    Args:
        obj (object)
        a_class (class):

    Returns:
        Boolean: True or False
    """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    else:
        return False
