#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mysquare = []
    for lists in my_list:
        if lists == search:
            mysquare.append(replace)
        else:
            mysquare.append(lists)
    return mysquare
