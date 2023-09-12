#!/usr/bin/python3
"""
Defines a function that deserializes an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Deserialize a JSON file and return the object."""
    with open(filename, "r", encoding="utf-8") as f:
        object = json.load(f)

    return object
