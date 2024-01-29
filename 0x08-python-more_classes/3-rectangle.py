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

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ Print the rectangle with the character #

            If width or height is equal to 0, return an empty string.

            Examples:
                >>> Rectangle = __import__('3-rectangle').Rectangle
                >>> my_rectangle = Rectangle(2, 4)
                >>> print(str(my_rectangle))
                ##
                ##
                ##
                ##
        """
        rect_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for row in range(self.__height):
            for col in range(self.__width):
                rect_str += "#"
            rect_str += "\n" if (row != self.__height - 1) else ""
        return rect_str
