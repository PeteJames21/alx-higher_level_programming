#!/usr/bin/python3
"""
Define a function that Checks if an object is an instance of a class that
inheritaed from a specific class.
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inheritaed from a_class."""
    if obj.__class__ == a_class:
        return False

    return isinstance(obj, a_class)
