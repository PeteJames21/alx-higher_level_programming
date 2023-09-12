#!/usr/bin/python3

"""
Define a class for serializing the attributes of an object.
"""


def class_to_json(obj):
    """Serialize the attributes of obj into a dict."""
    return obj.__dict__
