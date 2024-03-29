#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ciunt = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            ciunt += 1
        except (TypeError, IndexError, ValueError):
            pass
    print()
    return ciunt
