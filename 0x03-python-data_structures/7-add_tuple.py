#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = checker(tuple_a)
    tuple_b = checker(tuple_b)

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))


def checker(t=()):
    if len(t) < 2:
        if len(t) == 1:
            t = (t[0], 0)
        elif len(t) == 0:
            t = (0, 0)
    elif len(t) > 2:
        t = (t[0], t[1])

    return t
