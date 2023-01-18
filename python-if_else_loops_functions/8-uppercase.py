#!/usr/bin/python3
def uppercase(str):
    upper = {}
    for i in range(0, (len(str))):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = ord(str[i])
            num -= 32
            upper[i] = chr(num)
        elif i < (len(str) + 1):
            upper[i] = str[i]
        if i < len(str):
            print("{}".format(upper[i]), end="")
    print("\n")
