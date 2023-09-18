#!/usr/bin/python3
"""
Defines a Square class.
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Models a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of this class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} -"\
               f" {self.width}"

    @property
    def size(self):
        """Return the size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of self with the values in args.

        *args are parsed in this order: id, size, x, y.
        The number of *args should be 1 <= args <= len(args). Unknown
        attributes in *kwargs are ignored.
        """
        attrs = ["id", "size", "x", "y"]
        namespace = {"__builtins__": {}, "self": self}
        if args:
            for attr, value in zip(attrs, args):
                exec(f"self.{attr} = {value}", namespace, {})
        elif kwargs:
            for attr, value in kwargs.items():
                if attr in attrs:
                    exec(f"self.{attr} = {value}", namespace, {})

    def to_dictionary(self):
        """Return the dictionary representation of self."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
