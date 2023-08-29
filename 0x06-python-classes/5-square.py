#!/usr/bin/python3
"""Defines a Square type."""


class Square:
    """Models a square shape of fixed dimensions."""

    def __init__(self, size=0):
        """Initialize a square object of a given size.

        Args:
            size (int): size of the square - a positive integer >= 0
        """
        self.size = size

    def area(self):
        """Return the squared area of the Square object."""
        return self.size ** 2

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and set the size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
