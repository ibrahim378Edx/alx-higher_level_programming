#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    all possible multiples of  2  in the list
    """
    holder  = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            holder.append(True)
        else:
            holder.append(False)

    return holder
