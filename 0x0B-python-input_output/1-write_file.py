#!/usr/bin/python3
"""A 1-write_file.py module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file

    Args:
        filename: first parameter
        text: second parameter

    Return:
        the number of characters written:
    """

    with open(filename, 'w', encoding="utf-8") as f:
        num_text = f.write(text)
        return num_text
