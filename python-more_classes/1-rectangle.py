#!/usr/bin/python3
"""
This module contains the definition of
a Rectangle class
"""


class Rectangle:
    """Defines a rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
    """
    def __init__(self, width=0, height=0):
        if width is not type(int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.width = width
        if height is not type(int):
            raise TypeError('width must be an integer')
        elif height < 0:
            raise ValueError('width must be >= 0')
        else:
            self.height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if value is not type(int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value is not type(int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    