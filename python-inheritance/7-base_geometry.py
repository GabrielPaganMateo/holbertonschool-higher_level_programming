#!/usr/bin/python3
"""
Imports class Base Geometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(print("{} must be an integer".format(name)))
        elif value <= 0:
            raise ValueError(print("{} must be greater than 0").format(name))
