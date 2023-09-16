#!/usr/bin/python3
"""
Defines a base class for all classes in this project.
"""


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
