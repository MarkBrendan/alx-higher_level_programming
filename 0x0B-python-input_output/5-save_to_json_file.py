#!/usr/bin/python3
"""A 5-save_to_json_file.py module"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file\
            using a JSON representation:

    Args:
        my_ibj: first parameter
        filename: second parameter
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
