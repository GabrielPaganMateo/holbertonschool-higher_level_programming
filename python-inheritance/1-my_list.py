#!/usr/bin/python3
"""
Imports a class that inherits from list Class
"""


class MyList(list):
    """
        Contains method that prints a list but sorted
        Base Class:
            list (Built-in class)
    """
    def print_sorted(self):
        list_sorted = []
        for i in self:
            list_sorted.append(i)
        list_sorted.sort()
        print(list_sorted)
