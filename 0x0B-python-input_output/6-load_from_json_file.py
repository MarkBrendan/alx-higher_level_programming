#!/usr/bin/python3
"""A 6-load_from_json_file.py module"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”:

    Args:
        filename: first parameter
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
