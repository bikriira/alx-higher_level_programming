#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return my_list
    for i, value in enumerate(my_list):
        if i == idx:
            my_list[idx] = element
            return my_list
