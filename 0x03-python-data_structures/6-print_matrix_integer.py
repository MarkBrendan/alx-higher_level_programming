#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for num in matrix:
        for num1 in num:
            print("{}".format(num1), end=" ")
        print()
