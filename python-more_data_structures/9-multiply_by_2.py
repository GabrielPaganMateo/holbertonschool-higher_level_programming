#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    keys_multi = { name: age * 2 for name, age in a_dictionary.items() }
    return keys_multi
