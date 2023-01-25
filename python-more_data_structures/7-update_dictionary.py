#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    updated = {key: value}
    a_dictionary.update(updated)
    return a_dictionary
