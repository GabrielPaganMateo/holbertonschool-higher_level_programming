#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    diff1 = set_1 - set_2
    diff2 = set_2 - set_1
    diff_elements = list(diff1) + list(diff2)
    diff_elements = set(diff_elements)
    return diff_elements
