#!/usr/bin/python3
"""This module provides a Class
that defines a square"""


class Square:
    """Defines a square of a particular size
    Attributes:
        size (int): size of the square (private)
    Methods:
    __init__: initialize specific _Square__size
    attribute instance
    size: setter and getter properties,
    returns _Square__size or changes _Square__size"""
    def __init__(self, size=0, position=(0,0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                for j in range(self._Square__size):
                    print("#", end="")
                print()
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if type(value) is not tuple(value[0], value[1]):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position
