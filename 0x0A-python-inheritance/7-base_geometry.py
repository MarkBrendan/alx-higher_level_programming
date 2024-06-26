#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """an empty class BaseGeometry"""

    def area(self):
        """Define a area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define a integer_validator that validate integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0 or value == 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self.value = value
