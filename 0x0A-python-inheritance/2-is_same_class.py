#!/usr/bin/python3
"""
Check if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return obj.__class__ is a_class
