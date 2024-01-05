#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    index = 0
    arg_count = len(sys.argv) - 1

    if arg_count == 1:
        arg_str = "argument:"
    elif arg_count > 1:
        arg_str = "arguments:"
    else:
        arg_str = "arguments."

    print("{} {}".format(arg_count, arg_str))

    for arg in sys.argv:
        if index == 0:
            index += 1
            continue
        print("{}: {}".format(index, arg))
        index += 1
