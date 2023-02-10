#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        attrsDict = {}
        if attrs is type(list):
            for i in attrs:
                if i is type(str):
                    attrsDict[i] = self.i
                else:
                    break
            return attrsDict
        else:
            return self.__dict__
