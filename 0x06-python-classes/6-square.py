#!/usr/bin/python3
"""
    2-square.py
    Defines class Square
"""


class Square:
    """Class defined for square generation.

    Args:
        size (int): length of one side of square
        position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines


    Attributes:
        __size (int): length of one side of square
        __position (tuple) ((int), (int)): horizontal offset in spaces,
        vertical offset in newlines


    """
    def __init__(self, size=0, position=(0, 0)):
        """
            The constructor of Square,

            Args:
                size (int): size of the square
                __position (tuple) ((int), (int)): horizontal offset in spaces,
                vertical offset in newlines
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
        """Args:
            value (int): tuple of two positive integers

        Attributes:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        Raises:
            TypeError: if value is not a tuple of two positive ints

        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        """Calulates area of square.

        Attributes:
            __size (int): length of one side of square

        Returns:
            area (int): length of one side, squared

        """
        return self.__size ** 2

    def my_print(self):
        """Prints text representation of square in hash chars,
        horizontally and vertically offset by first and second int
        in __position, respectively.

        Attributes:
            __size (int): length of one side of square
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
        if self.__size is 0:
            print()
        else:
            for v_offset in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for h_offset in range(0, self.__position[0]):
                    print(" ", end="")
                for col in range(0, self.__size):
                    print("#", end="")
                print()
