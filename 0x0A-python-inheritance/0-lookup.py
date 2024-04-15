#!/usr/bin/python3
"""Function that return the available attribute"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj: the variable to lookup

    Return:
        Returns a list object
    """

    return dir(obj)
