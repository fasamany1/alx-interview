#!/usr/bin/python3
"""
Defines a function that returns a list
of lists of integers representing the 
Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of integers representing
    the Pascal Triangle of n and returns 
    an empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
