#!/usr/bin/python3
"""
Defines a function for printing the contents of a txt file to stdout.
"""


def read_file(filename=""):
    """Print filename contents to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
