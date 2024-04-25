#!/usr/bin/python3
"""Pascals Triangle"""


def pascal_triangle(num):
    """Function that returns a Pascal triangle"""
    triangle = []
    if num <= 0:
        return triangle

    for i in range(num):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
