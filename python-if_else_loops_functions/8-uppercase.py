#!/usr/bin/python3
def uppercase(str):
    upper = {}
    for i in range(0, len(str)):
        j = i + 1
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            num = ord(str[i])
            num -= 32
            upper[i] = chr(num)
        else:
            upper[i] = str[i]
        if j == len(str):
            print("{}".format(upper[i]), end="\n")
        elif str == "":
            print("")
        else:
            print("{}".format(upper[i]), end="")
