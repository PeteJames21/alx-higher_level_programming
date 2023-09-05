#!/usr/bin/python3
"""
Defines a function for dividing all elements of a matrix by a constant number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a constant.

    :param matrix: a 2x2 list of floats, ints, or a mix of both
    :param div: int/float to use as the divisor
    :return: the division result - a new matrix
    """
    # Validate the dtypes of the matrix elements.
    dtypes = {type(j) is int or float for i in matrix for j in i}
    if not all(dtypes):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # Ensure that each row is of the same size
    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    # Ensure that `div` is a number and is non-zero
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        result.append([round(i / div, 2) for i in row])

    return result
