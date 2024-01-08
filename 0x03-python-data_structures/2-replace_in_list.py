#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return None
    for i, value in enumerate(my_list):
        if i == idx:
            del my_list[idx]
            my_list.insert(idx, element)
            return my_list
