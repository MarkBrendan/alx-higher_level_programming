#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_lit = []
    for num in my_list:
        if num % 2 == 0:
            my_lit.append(True)
        else:
            my_lit.append(False)
    return my_lit
