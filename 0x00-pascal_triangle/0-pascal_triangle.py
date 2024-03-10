#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Implements the pascal triangle
    with formula (n+1)C(r) = (n)C(r - 1) + (n)C(r)"""
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for index in range(n):
        line = []
        for zndex in range(index + 1):
            if zndex == 0 or zndex == index:
                line.append(1)
            elif index > 0 and zndex > 0:
                line.append(triangle[index - 1][zndex - 1] +
                            triangle[index - 1][zndex])
        triangle.append(line)
    return triangle
