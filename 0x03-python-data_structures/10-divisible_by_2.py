#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        divisible = True if my_list[i] % 2 == 0 else False
        new_list.append(divisible)
    return new_list
