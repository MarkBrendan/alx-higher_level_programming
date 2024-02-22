#!/usr/bin/python3
"""module for writing file"""


def write_file(filename="", text=""):
    """Define a function the write text to a file"""
    with open(filename, 'w', encoding="utf-8") as flin:
        f = flin.write(text)
        return f
