#!/usr/bin/python3
"""
Define a class that models a rectangle.
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Models a rectangle."""
    def __init__(self, width, height):
        """Initialize an instance of this class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
