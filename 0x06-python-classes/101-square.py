#!/usr/bin/python3
"""Defines a Square type."""


class Square:
    """Models a square shape of fixed dimensions."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object of a given size.

        Args:
            size (int): size of the square - a positive integer >= 0
            position (tuple): the x-y position of the square
        """
        self.__str = ""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the x-y position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Validate and set the position of the square."""
        if not (isinstance(value, tuple) and len(value) == 2
                and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the squared area of the Square object."""
        return self.size ** 2

    def my_print(self):
        """Print the square."""
        self.__update_repr()
        print(self.__str)

    def __update_repr(self):
        """Update the square's string repr based on size and position."""
        self.__str = ""
        if self.size == 0:
            return
        self.__str += "\n" * self.position[1]
        self.__str += ((" " * self.position[0]) + ("#" * self.size) + "\n") \
            * self.size
        self.__str = self.__str.removesuffix("\n")  # Remove trailing newline

    def __str__(self):
        self.__update_repr()
        return self.__str
