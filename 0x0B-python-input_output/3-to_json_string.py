#!/usr/bin/python3
"""Provides a function to convert Python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """Converts a Python object to its JSON string representation.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON string representation of the input Python object.
    """
    return json.dumps(my_obj)
