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

    def to_json(self):
        """Serialize attributes of this class into a dict"""
        return self.__dict__
