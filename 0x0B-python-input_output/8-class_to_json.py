#!/usr/bin/python3

"""
Define a class for serializing the attributes of an object.
"""


def class_to_json(obj):
    """Serialize the attributes of obj into a dict."""
    d = {}
    for key, value in obj.__dict__.items():
        # Do not serialize private and special atrributes.
        if not key.startswith("__"):
            d[key] = value

    return d
