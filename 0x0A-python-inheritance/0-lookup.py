#!/usr/bin/python3
"""
Defines a class for inspecting attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of attributes and methods of an object."""
    return dir(obj)
