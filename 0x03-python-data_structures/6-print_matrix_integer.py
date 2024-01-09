#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, row_element in enumerate(row):
            spacer = " " if index != (len(row) - 1) else ""
            print("{:d}{}".format(row_element, spacer), end="")
        print()
