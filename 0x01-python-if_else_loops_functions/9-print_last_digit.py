#!/usr/bin/python3
def print_last_digit(number):
    z = abs(number) % 10
    print("{}".format(z), end="")
    return z