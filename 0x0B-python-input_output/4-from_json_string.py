#!/usr/bin/python3
"""
Deserialize a JSON-encoded string.
"""

import json


def from_json_string(my_str):
    """Deserialize a JSON string and return the object."""
    return json.loads(my_str)
