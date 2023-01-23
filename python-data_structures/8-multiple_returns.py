#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == None:
        x = (0, )
        return x

    length = len(sentence)
    first = sentence[:1]

    x = (length, first)

    return x
