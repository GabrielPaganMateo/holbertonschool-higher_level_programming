#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence == None:
        return None

    length = len(sentence)
    first = sentence[0]

    x = (length, first)

    return x
