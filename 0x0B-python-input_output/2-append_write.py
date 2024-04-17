#!/usr/bin/python3
"""A 2-append_write.py module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file

    Args:
        filename: first parameter
        text: second parameter

    Return:
        the number of characters written:
    """

    with open(filename, 'a', encoding="utf-8") as f:
        num_text = f.write(text)
        return num_text
