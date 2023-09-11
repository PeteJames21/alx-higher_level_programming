#!/usr/bin/python3
"""
Contains the definition of a Square class.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Models a square shape."""
    def __init__(self, size):
        """Initialize an instance of this class."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
