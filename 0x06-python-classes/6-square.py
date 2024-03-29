#!/usr/bin/python3
"""Hold the square class"""


class Square:
    """Class representing a square.

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
        """Initialize a square.

        Args:
            size (int, optional): Side of the square. Defaults to 0.
            position (tuple, optional): Horizontal and vertical offset.
                Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size getter, setter with same method name

        Returns:
            __size (int): length of one side, squared

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Args:
            value (int): length of one side of square

        Attributes:
            __size (int): length of one side of square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """__position getter, setter with same method name

        Returns:
            __position (tuple) ((int), (int)): horizontal offset in spaces,
            vertical offset in newlines

        """
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
        if (not isinstance(value, tuple)) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        x, y = value
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        if x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = (x, y)

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
