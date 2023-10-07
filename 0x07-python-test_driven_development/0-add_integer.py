#!/usr/bin/python3
"""Module for testing  doctest"""


def add_integer(a, b=98):
    """ functions that add ints or floats
        Arguments:
        @a: first integer
        @b: second integer
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
