#!/usr/bin/python3
"""
    Defines class Square
"""


class Square:
    """
        Defines a square by: (based on 1-square.py)

        Args:
            size: size of the square
    """
    def __init__(self, size=0):
        """
            The constructor of Square,
            setts the instance private attribute size
        """
        try:
            self.__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
