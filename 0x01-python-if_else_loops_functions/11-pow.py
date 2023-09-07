#!/usr/bin/python3
def pow(a, b):
    z = 1
    for i in range(0, abs(b)):
        if b > 0:
            z *= a
        else:
            z /= a
    return z
