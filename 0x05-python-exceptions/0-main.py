#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]
mylist = [1, 2, 3, 4]
newlist = []
z = [1,2,3,4]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(mylist, len(mylist)+10)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(newlist, 0)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(z, 0)
print("nb_print: {:d}".format(nb_print))

