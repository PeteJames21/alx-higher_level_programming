#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    squares = []
    for row in matrix:
        squares.append([i ** 2 for i in row])

    return squares
