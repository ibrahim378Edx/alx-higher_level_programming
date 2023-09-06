#!/usr/bin/python3
for i in range(1, 99):
    x = "".join(reversed(str(i)))
    if (i < int(x) or i < 10) and i != 89:
        print("{0:02d}, ".format(i), end="")
    if i == 89:
        print("89")
