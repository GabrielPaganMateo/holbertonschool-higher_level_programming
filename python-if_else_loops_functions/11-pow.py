#!/usr/bin/python3
def pow(a, b):
    x = a
    if b == 0:
        return (1)
    elif b > 0:
        for i in range(1, b):
            x *= a
    elif b < 0:
        b *= -1
        for i in range(1, b):
            x *= a
        y = 1/x
        return (y)
    return (x)
