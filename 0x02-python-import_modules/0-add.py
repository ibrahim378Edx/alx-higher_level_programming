#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    """

    adds 2 numbers together

    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
