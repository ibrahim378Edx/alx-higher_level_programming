#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    returns the weighted average of all values in tuple
    """
    if not my_list:
        return 0

    i = 0
    q = 0

    for tup in my_list:
        i += tup[0] * tup[1]
        q += tup[1]

    return (i / q)
