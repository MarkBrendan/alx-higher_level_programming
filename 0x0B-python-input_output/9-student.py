#!/usr/bin/python3
"""Class module"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialise the object"""
        self.first_nane = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """retrive the dict"""
            return self.__dict__
