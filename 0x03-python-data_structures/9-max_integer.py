#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    q = min(my_list)
    for item in my_list:
        if item > q:
            q = item

    return q
