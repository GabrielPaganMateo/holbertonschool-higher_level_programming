#!/usr/bin/python3
"""
Imports a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads text file (UTF8) and prints to stdout
        Args:
            filename (str): Name of text file
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
