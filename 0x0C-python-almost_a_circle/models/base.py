#!/usr/bin/puthon3
"""base.py module"""
import json


class Base:
    """A class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        with open(cls.__name__ + ".json", 'w', encoding='UTF-8') as f:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == {}:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(0, 0)
        dummy_instance.update(**dictionary)
        return dummy_instance
