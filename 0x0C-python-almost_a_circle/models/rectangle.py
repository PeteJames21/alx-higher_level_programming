#!/usr/bin/python3
"""
Defines a Rectangle class.
"""

from base import Base


class Rectangle(Base):
    """Models a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of this class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """Return the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height."""
        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """Return the value of the x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the x coordinate."""
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Return the value of the y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the y coordinate."""
        self.validate_attribute("y", value)
        self.__y = value

    @staticmethod
    def validate_attribute(name, value):
        """Check if an attribute has a valid value."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if name in ["x", "y"]:
            if value < 0:
                raise ValueError(f"{name} must be >= 0")
        elif name in ["width", "height"]:
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        # Invalid attribute names are not handled

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
