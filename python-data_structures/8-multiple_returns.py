#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is "" or sentence is None:
        x = (0, None)
        return x

    length = len(sentence)

    first = sentence[:1]
    x = (length, first)

    return x
