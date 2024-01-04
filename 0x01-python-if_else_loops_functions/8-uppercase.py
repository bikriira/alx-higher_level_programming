#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ord_char = ord(char)
        if ord_char in range(97, 123) or ord_char == 32:
            ord_char = 32 if ord_char == 32 else ord_char - 32
            real_char = "{:c}".format(ord_char)
        else:
            real_char = char
        print(real_char, end="")
    print()
