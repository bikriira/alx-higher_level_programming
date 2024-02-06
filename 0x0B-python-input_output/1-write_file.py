#!/usr/bin/python3
# Author: Iradufasha Bikri
"""Contains write_file()"""


def write_file(filename="", text=""):
    """Write the specified text to the specified file.

    Args:
        filename (str): The path to the file where the text will be written.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
