#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    a = list(tuple_a)
    b = list(tuple_b)

    if tuple_a == ():
        a = [0, 0]
    elif tuple_a == (tuple_a[0], ):
        a = [tuple_a[0], 0]
    elif tuple_a == (tuple_a[1]):
        a = [0, tuple_a[1]]
    if tuple_b == ():
        b = [0, 0]
    elif tuple_b == (tuple_b[0], ):
        b = [tuple_b[0], 0]
    elif tuple_b == (tuple_b[1]):
        b = [0, tuple_b[1]]

    value1 = a[0] + b[0]
    value2 = a[1] + b[1]

    c = (value1, value2)
    return c
