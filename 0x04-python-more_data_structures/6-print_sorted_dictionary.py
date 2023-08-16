#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a_dictionary by ordered keys."""
    keys_sorted = sorted(a_dictionary.keys())
    for key in keys_sorted:
        print(f"{key}: {a_dictionary[key]}")
