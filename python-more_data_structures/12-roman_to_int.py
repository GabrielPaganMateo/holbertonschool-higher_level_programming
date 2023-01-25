#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    elif roman_string is None:
        return 0

    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    _int = 0

    for char in roman_string:
        _int += roman_numeral[char]

    return _int
