#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the given integer.
    """
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Error: Invalid integer argument")
    sys.exit(1)
