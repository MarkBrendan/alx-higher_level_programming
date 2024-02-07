#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ciunt = 0
    for idx in range(x):
        try:
            int(my_list[idx])
            print("{:d}".format(my_list[idx]), end="")
            ciunt += 1
        except (IndexError, ValueError, TypeError):
            continue
    print()
    return ciunt
