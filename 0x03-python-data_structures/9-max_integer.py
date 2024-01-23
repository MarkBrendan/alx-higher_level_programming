#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    min_lit = my_list[0]
    for item in my_list:
        if item > min_lit:
            min_lit = item
            return min_lit
