#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """define the method"""
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
