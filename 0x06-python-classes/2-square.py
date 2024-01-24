#!/usr/bin/python3
"""
    2-square.py
    Defines class Square
"""


class Square:
    """
        Defines a square by: (based on 1-square.py)

        Attributes:
            size (int): size of the square
    """


    def __init__(self, size=0):
        """
            The constructor of Square,
            sets the instance private attribute size

            Args:
                size (int): size of the square
        """
        try:
            self.__size = int(size)
        except (ValueError, TypeError):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
