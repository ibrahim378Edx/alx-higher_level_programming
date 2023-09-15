#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    computes the square root of items in list
    """
    if not matrix:
        return None

    return list(list(map(lambda a: a*a, num_list)) for num_list in matrix)
