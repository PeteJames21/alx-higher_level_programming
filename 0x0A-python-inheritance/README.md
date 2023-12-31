# Python - Inhheritance

## 0-lookup.py
Write a function that returns the list of available attributes and methods of an object.

## 1-my_list.py
Write a class MyList that inherits from `list`:
- Public instance method: `def print_sorted(self)` that prints the list, but sorted (ascending sort)
- It is assumed that all the elements of the list will be of type `int`

## 2-is_same_class.py
Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

## 3-is_kind_of_class.py
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

## 4-inherits_from.py
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

## 5-base_geometry.py
Write an empty class `BaseGeometry`.

## 6-base_geometry.py
Augment the `BaseGeometry` from `5-base_geometry.py` with a public instance method `area()` that raises an `Exception` with the message "area() is not implemented"

## 7-base_geometry.py
Write a class `BaseGeometry` (based on `6-base_geometry.py`).
- Public instance method: `def area(self)` that raises an Exception with the message "area() is not implemented"
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
  - assume `name` is always a string
  - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  - if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`

## 8-rectangle.py
Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` must be private. No getter or setter
  - `width` and `height` must be positive integers, validated by `integer_validator`

## 9-rectangle.py
Augment `Rectangle` from `8-rectangle.py` with an `area()`, `str` and `print()` method:
- implement the `area()` method from the base class
- `print()` should print, and `str()` should return, the following rectangle description: `"[Rectangle] <width>/<height>"`

## 10-square.py
Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
- Instantiation with `size`: `def __init__(self, size)`
  - `size` must be private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`

## 11-square.py
Modify the __str__ method of the `Square` class from `10-square.py` to return the description: `"[Square] <width>/<height>"`

## 100-my_int.py
Write a class MyInt that inherits from `int`:
- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted

## 101-add_attribute.py
Write a function that adds a new attribute to an object if it’s possible.
- Raise a `TypeError` exception, with the message `"can't add new attribute"` if the object can’t have the new attribute
