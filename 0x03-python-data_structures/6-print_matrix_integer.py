#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for item in matrix:
            i = 1
            lt = len(item)

            for items in item:
                if i == lt:
                    print('{:d}'.format(items), end='')
                else:
                    print('{:d}'.format(items), end=' ')
                i += 1

            print()
