#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    converts a roman to int
    """
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    q = len(roman_string)
    value_int = r[roman_string[q-1]]
    for i in range(q - 1, 0, -1):
        current = r[roman_string[i]]
        previous = r[roman_string[i-1]]

        if previous >= current:
            value_int += previous
        else:
            value_int -= previous

    return value_int
