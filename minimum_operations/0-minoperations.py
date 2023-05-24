#!/usr/bin/python3
"""
The minOperations module offers a function
that calculates the minimum number of operations
needed to achieve a specific count of 'H' characters in a file.
This calculation is based on the available operations of Copy All and Paste.

"""
import math


def minOperations(n):
    """
    Find the minimum number of operations needed to
    obtain exactly n 'H' characters in the file.
    The method takes an integer n as a parameter.
    It returns the minimum number of operations
    required to achieve the desired count of 'H' characters.
    If n is negative or impossible to achieve, the method returns 0.

    """
    if n <= 0:
        return 0

    operations = 0

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            operations += i
            n = n // i

    if n > 1:
        operations += n

    return operations
