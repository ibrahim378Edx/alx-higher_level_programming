#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lists = []
    for i, q in a_dictionary.items():
        if q == value:
            lists.append(i)

    for i in lists:
        del a_dictionary[i]

    return a_dictionary
