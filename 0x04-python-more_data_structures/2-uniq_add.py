#!/usr/bin/python3
def uniq_add(my_list=[]):
    myuniq = set()
    for lists in my_list:
        myuniq.add(lists)
    return sum(myuniq)
