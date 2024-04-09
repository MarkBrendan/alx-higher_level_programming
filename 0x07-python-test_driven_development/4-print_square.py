#!/usr/bin/python3
"""A module that prints a square"""


def print_square(size):
    """A function that print prints a square with the character #

    Args:
        size: the integer


    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Print:
        square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("{}".format("#" * size))
