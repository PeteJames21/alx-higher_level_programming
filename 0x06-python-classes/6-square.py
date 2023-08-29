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
        if self.size == 0:
            print()
        else:
            # Shift the square down by y units
            print("\n" * self.position[1], end="")
            # Print the square, shifted to the right by x units
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
