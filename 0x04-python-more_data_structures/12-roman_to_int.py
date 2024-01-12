#!/usr/bin/python3
def roman_to_int(roman_string):
    exact_value = 0
    my_dict = {
        "M": 100, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
        }

    if (not isinstance(roman_string, str)) or roman_string is None:
        return 0
    if len(roman_string) == 1:
        return my_dict.get(roman_string, "Unkown num_char")

    for i in range(len(roman_string)):
        num = my_dict.get(roman_string[i], "Unkown num_char")
        if i < len(roman_string) - 1:
            num_next = my_dict.get(roman_string[i + 1], "Unkown num_char")
        else:
            num_next = 0

        if num < num_next:
            special_num = num_next - num
            exact_value += special_num
            break

        exact_value += num

    return exact_value
