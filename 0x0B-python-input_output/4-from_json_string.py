#!/usr/bin/python3
"""A 4-from_json_string.py module"""
import json


def from_json_string(my_str):
    """Write a function that returns an object\
            (Python data structure) represented by a JSON string

    Args:
        my_str: first parameter

    Return:
        returns an object (Python data structure) represented by a JSON string.
    """

    return json.loads(my_str)
