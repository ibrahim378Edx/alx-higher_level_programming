#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        z = ord(str[i])
        if (z >= 97 and z <= 122):
            z = z - 32
            str = str.replace(str[i], chr(z))
    print("{}".format(str))
