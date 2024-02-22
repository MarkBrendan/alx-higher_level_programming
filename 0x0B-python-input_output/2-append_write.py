#!/usr/bin/python3
"""module that append to a file"""


def append_write(filename="", text=""):
    """Define a function that append text to a file"""
    with open(filename, 'a', encoding="utf-8") as flin:
        f = flin.write(text)
        return f
