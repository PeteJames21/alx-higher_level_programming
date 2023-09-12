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
        if attrs:
            d = self.__dict__.copy()
            d_keys = list(d.keys())
            for key in d_keys:
                if key not in attrs:
                    d.pop(key, None)

            return d
        else:
            return self.__dict__
