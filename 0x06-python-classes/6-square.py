#!/usr/bin/python3
"""Hold the square class"""


class Square:
    """Class representing a square.

    Attributes:
        size (int): Length of one side of the square.
        position (tuple): Horizontal and vertical offset of the square.
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
        """Get the size of the square.

        Returns:
            int: The length of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The length of one side of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The horizontal and vertical offset of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): A tuple of two positive integers representing
                horizontal and vertical offset.

        Raises:
            TypeError: If the value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        x, y = value
        if x < 0 or y < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = (x, y)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print a text representation of the square with '#' characters.

        The output is horizontally and vertically offset by the first and
        second integers in the position attribute, respectively.
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
