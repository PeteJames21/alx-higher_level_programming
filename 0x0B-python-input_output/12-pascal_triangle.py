#!/usr/bin/python3
"""
Define a function for creating Pascal's triangle.
"""


def pascal_triangle(n):
    """Generate a list of lists representing pascal's triangle of size n."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[i - 1]
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)

    return triangle
