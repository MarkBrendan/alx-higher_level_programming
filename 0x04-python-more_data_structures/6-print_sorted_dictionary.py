#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    mydict = sorted(a_dictionary.keys())
    for sort in mydict:
        print("{}: {}".format(sort, a_dictionary[sort]))
