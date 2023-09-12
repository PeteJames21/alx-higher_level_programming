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
        """
        # attrs must be a list of strings, else all attributes are serialized.
        if attrs and type(attrs) is list and \
                all(type(key) is str for key in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
