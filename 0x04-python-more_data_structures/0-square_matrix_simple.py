#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mysquare = []
    for num in matrix:
        for num1 in num:
            mysquare.append(num1**2)
    return mysquare
