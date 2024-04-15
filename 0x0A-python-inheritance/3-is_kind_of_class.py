#!/usr/bin/python3
"""A Function that check for a class obect"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is\
            exactly an instance of the specified class

    Args:
        obj: the first parameter
        a_class: the second parameter

    Return:
        returns True if the object is exactly an instance\
                of the specified class ; otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
