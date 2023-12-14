#!/usr/bin/python3
"""
Write a method to determine the minimum
operations needed to achieve exactly
n H characters in a file,given n as input.
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1

    return result
