#!/usr/bin/python3
"""
Module to find max int
"""


def max_integer(list=[]):
    """Function to return max number
        If list empty return None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
