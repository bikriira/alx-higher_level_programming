#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print(int(my_list[i]), end="")
        except (ValueError, IndexError):
            pass
        else:
            count += 1
    print()
    return count
