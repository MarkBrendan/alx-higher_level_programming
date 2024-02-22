#!/usr/bin/python3

def read_file(filename=""):
    """Define a function the read text from a file"""

    with open(filename, encoding='utf-8') as flin:
        print(flin.read(), end=" ")
