#!/usr/bin/python3
"""This module provides a Class
that defines a square"""


class Square:
    """Defines a square of a particular size
    Attributes:
        size (int): size of the square (private)
    Methods:
    __init__: initialize specific square
    size attribute instance"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    def area(self):
        return self._Square__size ** 2
