#!/usr/bin/python3
"""
Write a method to determine the minimum operations
needed to achieve exactly n H characters in a file,
given n as input.
"""


def minOperations(n):
    result = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            result += divisor
            n //= divisor
        else:
            divisor += 1

    return result

