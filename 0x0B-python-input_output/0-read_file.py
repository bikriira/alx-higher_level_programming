#!/usr/bin/python3
# Author: Iradufasha Bikri
"""Contains the function read_file."""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the file to be read.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        PermissionError: If the user does not have permission to read the file.
        UnicodeDecodeError: If the file is not UTF-8 encoded.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
