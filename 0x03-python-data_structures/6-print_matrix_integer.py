#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        last = len(row) - 1  # The index of the last element in the row.
        for i, element in enumerate(row, start=0):
            print("{:d}".format(element), end="")
            if i != last:
                print(" ", end="")
            else:
                print()
