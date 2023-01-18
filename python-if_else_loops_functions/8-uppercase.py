#!/usr/bin/python3
def uppercase(str):
    size = len(str)
    upper = ""
    for i in range(0, size):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = ord(str[i])
            num -= 32
            upper += chr(num)
        else:
            upper += str[i]
    print("{:s}".format(upper))
