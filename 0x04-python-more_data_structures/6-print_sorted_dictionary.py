#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # my_dict = sorted(a_dictionary)
    # for key in my_dict:
    #    print("{}: {}".format(key, a_dictionary.get(key)))

    # ---- Other elegant way ----

    my_dict = sorted(a_dictionary.items())
    """
        returns a list of tuples, where each tuple contains a key-value pair
        from the dictionary.
    """

    for key, value in my_dict:
        """
            using tuple unpacking to extract the key and value from
            each tuple in sorted_dict during each iteration of the loop.
        """

        print("{}: {}".format(key, value))
