#!/usr/bin/python3
"""This module imports a function
that prints a first name followed by
a last name
"""


def say_my_name(first_name, last_name=""):
    """Function that prints full name
    Args:
    first_name (str):
    last_name (str):
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
