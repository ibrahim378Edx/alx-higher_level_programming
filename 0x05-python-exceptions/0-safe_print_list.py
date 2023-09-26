#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if  my_list == []:
        return 0
    if x == 0:
        print("{}".format(my_list[0]))
        return 1
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            print("")
            return i
    print("")
    return i + 1
