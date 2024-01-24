#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mysquare = []
    for row in matrix:
        myrow = []
        for element in row:
            myrow.append(element**2)
        mysquare.append(myrow)
    return mysquare
