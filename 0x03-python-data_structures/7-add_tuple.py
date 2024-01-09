#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    tuple_a.extend([0, 0])
    tuple_b.extend([0, 0])
    for index in range(2):
        new_tuple.append(tuple_a[index] + tuple_b[index])
    return tuple(new_tuple)
