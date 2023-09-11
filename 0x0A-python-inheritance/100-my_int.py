#!/usr/bin/python3
"""
Define a `MyInt` class that inherits from `int` and inverts the __eq__
and __ne__ methods.
"""


class MyInt(int):
    """A subclass of int that inverts the __eq__ and __ne__ methods."""

    def __eq__(self, other):
        """Invert the behavior of __eq__"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Invert the behavior of __ne__"""
        return not super().__ne__(other)
