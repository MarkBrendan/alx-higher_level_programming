#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    result = 0
    max_key = 0
    for item, value in a_dictionary.items():
        if value > result:
            result = value
            max_key = item
            return max_key
