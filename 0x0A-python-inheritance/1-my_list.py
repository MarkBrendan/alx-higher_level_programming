#!/usr/bin/python3
"""A Class that inherits from list"""


class MyList(list):
    """class MyList that inherits from list

    Args:
        list: the inherited class list

    Print:
        prints the list, but sorted (ascending sort)
    """

    def print_sorted(self):
        for element in self:
            if not isinstance(element, int):
                raise TypeError("list must be an int")
        print("{}".format(sorted(self)))
