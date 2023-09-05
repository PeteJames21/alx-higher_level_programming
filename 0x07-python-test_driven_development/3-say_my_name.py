#!/usr/bin/python3
"""
Define a function for printing a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """Print the full names given the first and last name."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("second_name must be a string")
    print(f"My name is {first_name} {last_name}")
