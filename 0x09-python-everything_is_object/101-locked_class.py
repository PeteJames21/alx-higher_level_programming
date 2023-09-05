#!/usr/bin/python3
"""
Define a class LockedClass with no class or object attribute, that prevents
the user from dynamically creating new instance attributes, except if
the new instance attribute is called `first_name`.
"""


class LockedClass:
    """A class that only allows one instance variable to be defined."""
    __slots__ = ["first_name"]
