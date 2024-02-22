#!/usr/bin/python3
"""An object to a text file, using a JSON representation"""


import json


def load_from_json_file(filename):
    """Define a function that returns an object represented by a JSON string"""
    with open(filename, 'r') as f:
        line = json.load(f)
        return line
