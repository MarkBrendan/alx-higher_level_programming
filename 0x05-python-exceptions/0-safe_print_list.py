#!/usr/bash/python3
def safe_print_list(my_list=[], x=0):
    ciunt = 0
    for idx in range(x):
        try:
            or idx in range(x):
            print("{}".format(my_list[idx]),  end="")
            ciunt += 1
        except IndexError:
            None
    print()
    return ciunt
