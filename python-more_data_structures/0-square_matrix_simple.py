#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    def squared(old_list):
        new_list = []
        for i in old_list:
            new_list.append(i * i)
        return new_list

    return list(map(squared, matrix))
