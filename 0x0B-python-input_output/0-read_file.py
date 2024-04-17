#!/usr/bin/python3
"""A 0-read_file.py module"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: first parameter


    Print:
        prints it to stdout.
    """

    with open('filename', 'r', encoding="utf-8") as f:
        for lin in f:
            print(lin, end="")
