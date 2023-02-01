#!/usr/bin/python3
"""This module contains a function
that divides all elements of a matrix
by any number (int or float)"""

def matrix_divided(matrix, div):
    """Function that divides every number
    in every list of a matrix by a specified
    number, returns the divided matrix
    Args:
        matrix (list): list of lists to be divided
        div (int or float): number to divide by"""
    for a_list in matrix:
        if type(a_list) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        for number in a_list:
            if type(number) is not int:
                if type(number) is not float:
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if len(matrix) > 1:
        for i in range(len(matrix)):
            if len(matrix[0]) != len(matrix[1]):
                raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int:
        if type(div) is not float:
            raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    def list_divided(old_list):
        new_list = []
        for i in old_list:
            new_list.append(round(i / div, 2))
        return new_list

    return list(map(list_divided, matrix))


    

