#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for idx in range(0, len(matrix)):
        for num in range(0, len(matrix[idx])):
            if num == len(matrix[idx]) - 1:
                print("{:d}".format(matrix[idx][num]))
            else:
                print("{:d} ".format(matrix[idx][num]), end="")
