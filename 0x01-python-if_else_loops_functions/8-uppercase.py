#!/usr/bin/pyhton3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{}".format(char), end="")
    print()
