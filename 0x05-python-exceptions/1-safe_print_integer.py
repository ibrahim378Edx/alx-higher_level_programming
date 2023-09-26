#!/usr/bin/python3
def safe_print_integer(value):
    try:
        x = value / 10
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
