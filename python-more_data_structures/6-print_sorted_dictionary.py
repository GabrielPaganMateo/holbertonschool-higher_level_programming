#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    key_list = list(a_dictionary.keys())
    key_list.sort()
    sorted_dict = {i: a_dictionary[i] for i in key_list}
    print(sorted_dict)
