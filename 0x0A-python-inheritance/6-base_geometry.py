#!/usr/bin/python3
"""
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """A base class for geometrical types."""

    def area(self):
        """Compute the area."""
        raise Exception("area() is not implemented")
