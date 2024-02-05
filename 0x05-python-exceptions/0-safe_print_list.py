#!/usr/bash/python3
def safe_print_list(my_list=[], x=0):
    ciunt = 0
    for idx in range(x):
        try:
            print(my_list[idx], end="")
            ciunt += 1
        except:
            break
    print()
    return ciunt
