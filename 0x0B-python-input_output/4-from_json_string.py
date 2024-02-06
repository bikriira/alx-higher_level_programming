#!/usr/bin/python3
"""Provides a function to convert JSON to Python objects."""

import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
