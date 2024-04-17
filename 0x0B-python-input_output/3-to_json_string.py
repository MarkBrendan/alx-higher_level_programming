#!/usr/bin/python3
import json
"""A 3-to_json_string.py module"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object

    Args:
        my_obj: first parameter

    Return:
        returns the JSON representation of an object (string).
    """

    return json.dumps(my_obj)
