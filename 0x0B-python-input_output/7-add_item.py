#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
import sys
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []
try:
    my_list = load_from_json_file("add_item.json")
except (FileNotFoundError, json.JSONDecodeError):
    with open("add_item.json", "w", encoding="utf-8") as file:
        save_to_json_file(my_list, "add_item.json")

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")
