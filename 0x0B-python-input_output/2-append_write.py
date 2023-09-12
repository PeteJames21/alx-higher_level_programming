#!/usr/bin/python3

"""
Define a function for appending a string to a file.
"""


def append_write(filename="", text=""):
    """Append text to the given file and return number of bytes written."""
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)

    return n
