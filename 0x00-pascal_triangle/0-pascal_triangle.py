#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s triangle of n.
"""
'''Pascal triangle formula is (n+1)C(r) = (n)C(r - 1) + (n)C(r). It means that the number of ways to choose r items out of a total of n + 1 items is the same as adding the number of ways to choose r - 1 items out of a total of n items and the number of ways to choose r items out of a total of n items.'''


def pascal_triangle(n):
    """Implements the pascal triangle."""
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for index in range(n):
        line = []
        for jndex in range(index + 1):
            if jndex == 0 or jndex == index:
                line.append(1)
            elif index > 0 and jndex > 0:
                line.append(triangle[index - 1][jndex - 1] +
                            triangle[index - 1][jndex])
        triangle.append(line)
    return triangle
