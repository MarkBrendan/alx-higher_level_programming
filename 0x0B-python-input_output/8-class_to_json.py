#!/usr/bin/python3

def class_to_json(obj):
    """Define a function that returns an object represented by a JSON string"""
    return obj.__dict__
