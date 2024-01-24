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
            position=(0, 0):
    """
    def __init__(self, size=0, position=(0, 0)):
        """
            The constructor of Square,

            Args:
                size (int): size of the square
                position=(0, 0):
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not (isinstance(x, int) and isinstance(y, int)) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (x, y)

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for row in range(self.__size):
            print(" " * self.__position[0], end="")
            for col in range(self.__size):
                print("#", end="", sep="")
            print()
        if self.__size <= 0:
            print()
