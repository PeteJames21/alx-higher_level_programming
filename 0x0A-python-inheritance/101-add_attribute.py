#!/usr/bin/python3
"""
Defines a function for adding an attribute to an object.
"""


def add_attribute(obj, attr_name, value):
    """Add an attribute to an object."""
    # Immutable types do not have a __dict__ attribute
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, value)
    else:
        raise TypeError("can't add new attribute")
