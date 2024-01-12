#!/usr/bin/python3
def weight_average(my_list=[]):
    for left, right in my_list:
        uper_statement += left * right
        base_statement += right
    return uper_statement / base_statement
