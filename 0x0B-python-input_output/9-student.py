#!/usr/bin/python3
"""Class module"""


class Student:
    def __init__(self, first_name, last_name, age):
        """my class"""
        self.first_nane = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """retrive the dict"""
            self.__dict__
