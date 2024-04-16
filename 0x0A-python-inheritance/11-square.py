#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """an class BaseGeometry"""

    def area(self):
        """Define a area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Define a integer_validator that validate integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self.value = value


class Rectangle(BaseGeometry):
    """An inherited call Rectangle"""

    def __init__(self, width, height):
        """initialise a constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """An inherited class Square"""

    def __init__(self, size):
        """initialise a constructor"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
