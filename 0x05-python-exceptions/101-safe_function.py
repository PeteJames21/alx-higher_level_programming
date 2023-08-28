#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """Execute the function `fct` with the arguments in *args."""
    try:
        result = fct(*args)
    except Exception as e:
        result = None
        stderr.write(f"Exception: {e}\n")

    return result
