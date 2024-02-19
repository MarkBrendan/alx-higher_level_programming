#!/usr/bin/python3
"""A method that compare an object"""


def inherits_from(obj, a_class):
    """define the method"""

    obj_class = type(obj)

    while obj_class is not None:
        if issubclass(type(obj), a_class) and type(obj) != a_class:
            return True
        obj_class = obj_class.__base__ if hasattr(obj_class, '__base__') else None

    return False
