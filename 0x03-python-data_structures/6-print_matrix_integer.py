#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for row_element in row:
            print("{:d}".format(row_element), end=" ")
        print()
