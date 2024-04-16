#!/usr/bin/python3
"""A class MyInt"""


class MyInt(int):

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
