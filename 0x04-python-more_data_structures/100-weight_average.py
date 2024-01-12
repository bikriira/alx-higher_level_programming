#!/usr/bin/python3
def weight_average(my_list=[]):
    uper_statement = 0
    base_statement = 0
    for left, right in my_list:
        uper_statement += left * right
        base_statement += right
    return uper_statement / base_statement
