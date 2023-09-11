#!/usr/bin/python3
"""
Defines a BaseGeometry class.
"""


class BaseGeometry:
    """A base class for geometrical types."""

    def area(self):
        """Compute the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if a value is a valid dimension for this class."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
