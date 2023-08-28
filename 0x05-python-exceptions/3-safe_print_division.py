#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide a by b then print and return the result."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
