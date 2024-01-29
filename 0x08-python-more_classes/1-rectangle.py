#!/usr/bin/python3
# 0-rectangle.py
"""Contains the rectangle clas which basically do nothing"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Calls the coresponding setter with given arguments

        Args:
            width (int): An integer grater than 0
            height (int): An integer grater than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width property.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height property.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height property.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
