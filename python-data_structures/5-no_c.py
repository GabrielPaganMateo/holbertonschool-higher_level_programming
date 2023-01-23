#!/usr/bin/python3


def no_c(my_string):
    new_string = my_string[:]
    print(my_string)
    print(new_string)

    for idx in range(0, len(my_string) - 1):
        print(idx)
        if my_string[idx] == "c":
            new_string = my_string[:idx] + my_string[idx + 1:]
        elif my_string[idx] == "C":
            if idx == 0:
                new_string = my_string[idx + 1:]
            else:
                new_string = my_string[:idx] + my_string[idx + 1:]


    return new_string
