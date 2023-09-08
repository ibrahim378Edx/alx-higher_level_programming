#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """
    Prints passed arguments

    """
    argument = sys.argv
    arg = len(argument) - 1

    if arg > 1:
        print(arg, 'arguments:')
        for i in range(1, arg + 1):
            print('{:d}: {}'.format(i, arg[i]))
    elif arg == 1:
        print(arg, 'argument:')
        for i in range(1, arg + 1):
            print('{:d}: {}'.format(i, arg[i]))
    elif arg == 0:
        print(arg, 'arguments.')
