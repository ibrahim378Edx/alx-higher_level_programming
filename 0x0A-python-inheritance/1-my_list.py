#!/usr/bin/python3
"""
prints a list in ascending order
"""


class MyList(list):
    """
    A class
    """

    def print_sorted(self):
        """
        Prints a list in ascending order

        Sort a list and then prints on the output
        """

        if issubclass(MyList, list):
            print(sorted(self))
