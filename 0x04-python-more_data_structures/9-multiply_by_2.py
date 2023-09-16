#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a dict with with  multiplied by 2
    """
    new = {x: (a_dictionary[x] * 2) for x in a_dictionary}
    return new
