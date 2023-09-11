#!/usr/bin/python3
"""
Check if an object is a direct/indirect instance of a specific class
"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class."""
    return isinstance(obj, a_class)
