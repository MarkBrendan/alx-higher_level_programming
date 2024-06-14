#!/usr/bin/python3
"""class MagicClass that corresponds to the given bytecode"""

import math


class MagicClass:
    """A magic clwss"""
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.__radius
