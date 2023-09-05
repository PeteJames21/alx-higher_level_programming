#!/usr/bin/python3
"""
Define a function for printing a square with the character `#`
"""


def print_square(size):
    """Print a square of given size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        s = "\n".join(["#" * size for _ in range(size)])
        print(s)
