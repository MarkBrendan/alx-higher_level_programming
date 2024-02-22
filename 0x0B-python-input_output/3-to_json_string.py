#!/usr/bin/python3
"""module that gives the JSON representation of an object"""

import json


def to_json_string(my_obj):
    """Define a function that gives the JSON representation of an obj"""
    return json.dumps(my_obj)
