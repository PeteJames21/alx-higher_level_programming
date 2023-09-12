#!/usr/bin/python3
"""
Define a self-serializable class.
"""


class Student:
    """A self-serializable class."""

    def __init__(self, first_name, last_name, age):
        """Initialize an instance of this class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Serialize attributes of this class into a dict.

        :param attrs: list of attrs to serialize. Serialize all if attrs=None
        :return: a dict of attributes of this class
        """
        # attrs must be a list of strings, else all attributes are serialized.
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Use a dict to set values of attributes of Student objects."""
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])
