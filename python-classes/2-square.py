#!/usr/bin/python3
"""This module provides a class that
defines a square"""


class Square:
    """Defines a square
    Attribute:
        size (int): size of the square, private"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
