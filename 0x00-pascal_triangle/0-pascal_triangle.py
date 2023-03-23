#!/usr/bin/python3
"""
A function that returns a list of integers
Representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    """
    Creates a list of integers representing Pascal's triangle

    Parameters:
        n(int): number of rows of pascal's triangle to create
    return: representation of Pascal's triangle
    """
    if type(n) is not int:
        raise TypeError("n must be an integer")
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(1+i):
            if j == 0:
                row.apppen(1)
            elif j == i:
                ow.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(arr)
    return triangle
