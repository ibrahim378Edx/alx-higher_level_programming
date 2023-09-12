#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    q = min(my_list)
    for i in my_list:
        if i > q:
            q = i

    return q
