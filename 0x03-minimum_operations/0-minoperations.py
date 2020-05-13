#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in a file

    resoluton method: look at the output for the first n = 15 strings
    observe that if n is prime number, num_op = n
    if n is not prime number, decompose n into prime numbers, sum
    the prime numbers and return num_op = sum
    """
    if n <= 1:
        return 0
    num_op = []
    for i in range(2, int(n) + 1):
        while (n % i) == 0:
            num_op += [i]
            n = n / i
    return sum(num_op)
