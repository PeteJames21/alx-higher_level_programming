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
