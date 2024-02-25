#!/usr/bin/python3
def add_integer(a, b=98):
    """Returns an integer: the addition of a and b
    a and b must be integers or floats
    Raise:
        TypeError: a must be an integer or b must be an integer
        """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(a must be an integer)
    elif not isinstance(b, (int, float)):
        raise TypeError(b must be an integer)
    return (int(a) + int(b))
