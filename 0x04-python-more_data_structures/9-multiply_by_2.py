#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    for item, value in a_dictionary.items():
        result[item] = value * 2
    return result
