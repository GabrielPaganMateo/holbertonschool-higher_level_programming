#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for idx in range(0, (len(matrix) - 1)):
        for num in range(0, (len(matrix[idx]) - 1)):
            print(matrix[idx][num])
