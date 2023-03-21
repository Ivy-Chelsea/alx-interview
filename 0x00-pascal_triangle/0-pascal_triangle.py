#!/usr/bin/python3
"""
A function that returns a list of integers
Representing the Pascal's triangle of n
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return [num for row in triangle for num in row]
