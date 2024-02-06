#!/usr/bin/python3
"""Provides a function to load Python objects from a JSON file."""

import json


def load_from_json_file(filename):
    """Load a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
