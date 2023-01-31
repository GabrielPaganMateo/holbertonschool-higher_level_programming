#!/usr/bin/python3
"""Module imports the add_integer function, adds two ints"""

def add_integer(a, b=98):
    try:
        if type(a) is not int:
            if type(a) is not float:
                raise TypeError("a must be an integer")
        if type(b) is not int:
            if type(b) is not float: 
                raise TypeError("b must be an integer")
    except Exception as e:
        return e
    else:
        a = int(a)
        b = int(b)
        return a + b
