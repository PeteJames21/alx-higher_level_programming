#!/usr/bin/python3
"""
Define a `MyInt` class that inherits from `int` and inverts the __eq__
and __ne__ methods.
"""


def MyInt(int):
    """A subclass of int that inverts the __eq__ and __ne__ methods."""

    def __eq__(self, other):
        """An inversion of int.__eq__."""
        return not super().__eq__(self, other)

    def __ne__(self, other):
        """An inversion of int.__ne__."""
        return not super().__ne__(self, other)
