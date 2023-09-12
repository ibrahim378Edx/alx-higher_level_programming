#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    w = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return w

    w[idx] = element
    return w
