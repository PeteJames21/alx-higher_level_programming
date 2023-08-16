#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """Delete the specified key from a_dictionary in place."""
    if key in a_dictionary:
        a_dictionary.pop(key)

    return a_dictionary
