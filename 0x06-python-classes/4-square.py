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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(value)

    def area(self):
        return self.__size ** 2
