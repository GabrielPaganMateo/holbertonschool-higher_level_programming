#!/usr/bin/python3
"""
Imports the function is_same_class
"""


def is_same_class(obj, a_class):
    """
        Returns True if the object is exactly an
        instance of the specified class otherwide
    """
    if isinstance(obj) is a_class:
        return True
    else:
        return False
