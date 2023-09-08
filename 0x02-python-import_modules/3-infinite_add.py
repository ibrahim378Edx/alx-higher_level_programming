#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg = sys.argv
    args = len(arg)
    sum = 0

    if args > 1:
        for i in range(1, args):
            sum += int(arg[i])

    print(sum)
