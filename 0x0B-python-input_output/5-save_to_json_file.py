#!/usr/bin/python3
"""Provides a function to save Python objects to a JSON file."""

import json


def save_to_json_file(my_obj, filename):
    """Save a Python object to a JSON file.

    Args:
        my_obj: The Python object to be saved to the file.
        filename (str): The path to the file where the object will be saved.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
