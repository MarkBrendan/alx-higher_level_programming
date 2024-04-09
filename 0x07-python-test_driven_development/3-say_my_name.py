#!/usr/bin/python3
"""A module that print the first and last name"""


def say_my_name(first_name, last_name=""):
    """A function that print the first and last name

    Args:
        first_name: first string
        last_name: second string


    Raise:
        TypeError: first_name must be a string or last_name must be a string

    Print:
        the first and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
