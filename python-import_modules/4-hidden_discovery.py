#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

string = ""
ls = dir(hidden_4)

for i in range(0, len(ls)):
    string = ls[i]
    if string[0:2] != "__" and string[-2:] != "__":
        print(string)
