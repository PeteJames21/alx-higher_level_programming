#!/usr/bin/python3
"""
Defines a function that writes an object to a file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """Serialize an object to a file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
