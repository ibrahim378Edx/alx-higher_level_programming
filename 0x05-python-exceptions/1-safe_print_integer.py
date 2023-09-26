#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = int(value)
        print("{}".format(x))
    except ValueError:
        return False
    else:
        return True
