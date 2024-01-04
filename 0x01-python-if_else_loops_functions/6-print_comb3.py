#!/usr/bin/python3
for left in range(0, 9):
    for right in range(0, 10):
        if right > left:
            if "{}{}".format(left, right) != "89":
                print("{}{}".format(left, right), end=", ")
print("{}".format(89))
