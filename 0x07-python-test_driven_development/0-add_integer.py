#!/usr/bin/python3
"""A module that adds two number and return the value"""


def add_integer(a, b=98):
    """add_integer function add of a and b
    a and b must be integers or floats

    Raise:
        TypeError: a must be an integer or b must be an integer

        Args:
            a: first integer
            b: second integer with a place holder of 98

        Return:
            return the value. a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
