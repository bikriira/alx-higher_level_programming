#!/usr/bin/python3
"""contains the class Student"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of a Student instance.

        If `attrs` is a list of strings, returns only the attributes
        listed in `attrs` for the instance.

        Args:
            attrs (list): List of attributes to include in the dictionary.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        obj_dict = self.__dict__
        new_dict = {}

        if attrs is None:
            return obj_dict

        for i in range(len(attrs)):
            value = obj_dict.get(attrs[i])
            if value:
                new_dict[attrs[i]] = value

        return new_dict
