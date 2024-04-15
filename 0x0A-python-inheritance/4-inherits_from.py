#!/usr/bin/python3
"""A Function that check for a class obect"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is\
            exactly an instance of the specified class

    Args:
        obj: the first parameter
        a_class: the second parameter

    Return:
        returns True if the object is exactly an instance\
                of the specified class ; otherwise False.
    """

    
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
