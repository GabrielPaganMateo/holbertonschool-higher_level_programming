#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    elif roman_string is None:
        return 0
    roman_numeral = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}

    num_list = []
    for char in roman_string:
        num_list.append(roman_numeral[char])

    _int = 0
    prev_number = 0
    for number in reversed(num_list):
        if prev_number != 0 and number < prev_number:
            _int -= number
            continue
        _int += number
        prev_number = number
    return _int
