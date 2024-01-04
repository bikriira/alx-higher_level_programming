#!/usr/bin/python3
for char in range(97, 123):
    if char not in (113, 101):
        print("{:c}".format(char), end="")
