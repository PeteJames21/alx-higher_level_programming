#!/usr/bin/python3
"""
Defines a base class for all classes in this project.
"""

import json
import os
import csv
import turtle


class Base:
    """The base class for all classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of this class."""
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON representation of a list of dicts."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the serialized instances of this class to a JSON file.

        :param list_objs: a list of objects that inherit from Base. They must
        implement a `to_dictionary` method.
        """
        list_dicts = []
        filename = f"{cls.__name__}.json"
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON list of dicts."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of this class with the specified attributes."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)  # Create a Rectangle
            else:
                obj = cls(1)  # Create a Square
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """Deserialize instances of this class from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        list_objects = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())

        for d in list_dicts:
            list_objects.append(cls.create(**d))

        return list_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save the serialized instances of this class to a CSV file.

        :param list_objs: a list of objects that inherit from Base. They must
        implement a `to_dictionary` method.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances of this class from a CSV file."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fields = ["id", "width", "height", "x", "y"]
            else:
                fields = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fields)
            list_dicts = [dict([k, int(v)] for k, v in d.items())
                          for d in list_dicts]

        return [cls.create(**d) for d in list_dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangle and Square instances using the turtle module.

        :param list_rectangles: a list of Rectangle instances
        :param list_squares: a list of Square instances
        """
        turt = turtle.Turtle()
        turt.pensize(5)
        turt.shape("square")
        turt.screen.bgcolor("black")

        # Draw the rectangles
        turt.color("white")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.up()

        # Draw the squares
        turt.color("red")
        for sq in list_squares:
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.down()

        turt.hideturtle()
        turtle.exitonclick()
