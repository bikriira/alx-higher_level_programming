#!/usr/bin/python3
def roman_to_int(roman_string):
    exact_value = 0
    my_dict = {
        "M": 100, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1, "U": 0
    }

    if (not isinstance(roman_string, str)) or roman_string is None:
        return 0

    roman_string = list(roman_string)

    if len(roman_string) == 1:
        return my_dict.get(roman_string[0], "Unkown num_char")

    for i in range(len(roman_string)):
        num = my_dict.get(roman_string[i], "Unkown num_char")
        if i < len(roman_string) - 1:
            num_next = my_dict.get(roman_string[i + 1], "Unkown num_char")
            if num < num_next:
                if roman_string[i] == "U":
                    continue
                roman_string[i + 1] = "U"
                special_num = num_next - num
                exact_value += special_num
                continue

        exact_value += num

    return exact_value
