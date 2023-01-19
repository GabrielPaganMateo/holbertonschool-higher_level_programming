#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

for i in range(0, len(dir(hidden_4))):
    str = hidden_4[i]
    if str[0:2] != "__" and str[-2:] != "__":
        print(hidden_4[i])
