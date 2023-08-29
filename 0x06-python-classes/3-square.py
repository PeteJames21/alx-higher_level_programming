#!/usr/bin/python3#!/usr/bin/python3
"""Defines a Square type."""


class Square:
    """Models a square shape of fixed dimensions."""

    def __init__(self, size=0):
        """Initialize a square object of a given size.

        Args:
            size (int): size of the square - a positive integer >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Return the squared area of the Square object."""
        return self.__size ** 2
