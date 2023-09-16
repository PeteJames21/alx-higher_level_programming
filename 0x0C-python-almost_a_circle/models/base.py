#!/usr/bin/python3
"""
Defines a base class for all classes in this project.
"""

import json


class Base:
    """The base class for all classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of this class."""
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dicts."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the serialized instances of this class to a JSON file.

        :param list_objs: a list of objects that inherit from Base. They must
        implement a `to_dictionary` method.
        """
        list_dicts = []
        filename = f"{cls.__name__}.json"
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)
