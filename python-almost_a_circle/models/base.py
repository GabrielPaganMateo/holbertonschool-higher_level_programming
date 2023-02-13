#!/usr/bin/python3
"""
Module with Class 'Base'
"""


class Base:
    """
    'base' of all the other classes in this project,
    the goal is to manage id attribute in all future
    classes and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
