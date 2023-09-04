#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Models a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle with the provided dimensions"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def width(self):
        """Return the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of a rectangle."""
        s = ""
        if self.width != 0 and self.height != 0:
            s += "\n".join("#" * self.__width for j in range(self.__height))
        return s

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
