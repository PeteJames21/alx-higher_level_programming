#!/usr/bin/python3
"""Defined a class that models a circle."""
from math import pi


class MagicClass:
    """Represents a circle."""
    def __init__(self, radius=0):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * (self.__radius ** 2)

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * pi * self.__radius
