#!/usr/bin/python3
"""
Defines a class, MyList, that inherits from the builtin list type and
includes a method for printing its sorted elements.
"""


class MyList(list):
    """An extension of the builtin list type."""

    def __init__(self, *args, **kwargs):
        """Initialize an instance of this class."""
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))
