#!/usr/bin/python3
"""
Imports the class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class that defines the methods and
    fields of a Rectangle 
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(width)
        BaseGeometry.integer_validator(height)
        self._Rectangle__width = width
        self._Rectangle__height = height
