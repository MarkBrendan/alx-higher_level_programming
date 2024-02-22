#!/usr/bin/python3
import json

"""module that gives the JSON representation of an object"""


def to_json_string(my_obj):
    """Define a function that gives the JSON representation of an obj"""
    return json.dumps(my_obj)
