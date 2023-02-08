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
            try:
                raise TypeError(print("{} must be an integer".format(name)))
            except Exception:
                pass
        elif value <= 0:
            try:
                raise ValueError(print("{} must be greater than 0").format(name))
            except Exception:
                pass
