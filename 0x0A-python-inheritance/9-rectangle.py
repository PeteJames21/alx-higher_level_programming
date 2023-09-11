#!/usr/bin/python3
"""
Define a class that models a rectangle.
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


class Rectangle(BaseGeometry):
    """Models a rectangle."""
    def __init__(self, width, height):
        """Initialize an instance of this class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of a Rectangle instance."""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def print(self):
        """Print the string representation of a Rectangle instance."""
        print(self.__str__())
