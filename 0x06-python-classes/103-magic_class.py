#!/usr/bin/python3
from math import pi


class MagicClass:
    def __init__(self, radius):
        if type(radius) not in (int, float):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def circumference(self):
        return 2 * pi * self.__radius
