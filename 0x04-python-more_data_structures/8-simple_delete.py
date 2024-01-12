#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key, None) is None:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
