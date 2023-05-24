#!/usr/bin/python3
import math

def minOperations(n):
    if n == 0:
        return 0

    operations = 0
    clipboard = 1  # Start with a single 'H' in the clipboard
    characters = 1  # Start with a single 'H' in the file

    while characters < n:
        if n % characters == 0:
            clipboard = characters  
        # If the number of characters is a divisor of n, update the clipboard

        characters += clipboard
        operations += 1

    if characters == n:
        return operations
    else:
        return 0  # n is impossible to achieve


# Testing the example case
n = 9
print(minOperations(n))
