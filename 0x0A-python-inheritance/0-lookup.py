#!/usr/bin/python3
# 0x0A-python-inheritance/0-lookup.py
""" Conatins lookup function """


def lookup(obj):
    """
        Returns the list of available attributes and methods of an object

        Args:
            obj: The one to be looked up.

        Returns:
            list: A list containing the names
                  of attributes and methods of the object.
    """
    return dir(obj)
