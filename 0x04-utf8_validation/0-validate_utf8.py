#!/usr/bin/python3
"""
Method to determine if given data represents valid UTF-8 encoding
Data set can contain multiple characters 
or will represent a list of integers
"""


def validUTF8(data):
    """
    Prototype: def validUTF8(data)
    Returns True if valid else return False
    """
    count = 0

    for bit in data:
        binary = bin(bit).replace('0b', '').rjust(8, '0')[-8:]
        if count == 0:
            if binary.startswith('110'):
                count = 1
            if binary.startswith('1110'):
                count = 2
            if binary.startswith('11110'):
                count = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            count -= 1

    if count != 0:
        return False

    return True
