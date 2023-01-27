#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as Err:
        pass
    finally:
        if b != 0:
            print("Inside Result: {}".format(result))
        else:
            result = Err
            print("Inside Result: {}".format(result))
        return result