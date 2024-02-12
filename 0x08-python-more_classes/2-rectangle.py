#!/usr/bin/python3
"""Defination of a class"""


class Rectangle:
    """The rectangle feature"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """set the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

        @property
        def height(self):
            """set the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        def area(self):
            """Return the area of the Rectangle."""
            return (self.__width * self__height)

        def perimeter(self):
            """Return the perimeter of the Rectangle."""
            if width == 0 or height == 0:
                return (0)
            else:
                return (2 * (self.__width + self__height))
