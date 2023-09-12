#!/usr/bin/python3
"""
Define a function for creating Pascal's triangle.
"""


def pascal_triangle(n):
    """Generate a list of lists representing pascal's triangle of size n."""

    def factorial(n):
        """Return the factorial of n."""
        if n < 0:
            raise ValueError("n must be >= 0")

        if (n == 0 or n == 1):
            return 1

        else:
            return (n * factorial(n - 1))

    triangle = []
    if n <= 0:
        return triangle

    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            term = factorial(i) / (factorial(j) * factorial(i - j))
            row.append(int(term))  # Convert float to int

        triangle.append(row)

    return triangle
