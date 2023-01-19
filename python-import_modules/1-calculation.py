#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
a = 10
b = 5
plus = "+"
minus = "-"
multi = "*"
divid = "/"
print("{} {} {} = {}".format(a, plus, b, add(a, b)))
print("{} {} {} = {}".format(a, minus, b, sub(a, b)))
print("{} {} {} = {}".format(a, multi, b, mul(a, b)))
print("{} {} {} = {}".format(a, divid, b, div(a, b)))
