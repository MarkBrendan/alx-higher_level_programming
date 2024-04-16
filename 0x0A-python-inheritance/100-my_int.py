#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):
    """Define MyInt"""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
