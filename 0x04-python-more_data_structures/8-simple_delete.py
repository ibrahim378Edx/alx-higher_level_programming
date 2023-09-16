#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes keys in a dict
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
