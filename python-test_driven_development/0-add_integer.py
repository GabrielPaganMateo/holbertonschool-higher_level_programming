#!/usr/bin/python3
"""Module imports the add_integer function,
adds two ints or two floats, floats will be
converted to ints before addition. The first
argument must always be included, but second
argument can be None as it will default to 98"""


def add_integer(a, b=98):
    """Function that adds two integers
        a (int): first integer
        b (int): second integer, default value is 98"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
