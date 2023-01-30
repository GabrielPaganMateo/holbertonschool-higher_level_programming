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

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

        if (type(position) is not tuple or len(position) < 2 or
            type(position[0]) is not int or type(position[1]) is not int or
                position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self._Square__position = position

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
            for h in range(self._Square__position[1]):
                print()
            for i in range(self._Square__size):
                k = 0
                while k < self._Square__position[0]:
                    print(" ", end="")
                    k += 1
                for j in range(self._Square__size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) < 2
            or type(value[0]) is not int or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self._Square__position = value
