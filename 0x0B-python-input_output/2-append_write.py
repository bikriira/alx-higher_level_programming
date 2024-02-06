#!/usr/bin/python3
""" Author: Iradufasha Bikri """


def append_write(filename="", text=""):
    """Append the specified text to the end of the specified file.

    Args:
        filename (str): The path to the file where the text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
