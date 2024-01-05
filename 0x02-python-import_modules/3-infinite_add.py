#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv)
    index, arg_sum = [0, 0]
    for arg in sys.argv:
        if index == 0:
            index += 1
            continue
        arg_sum += int(arg)
        index += 1
    print(arg_sum)
