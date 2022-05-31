#!/usr/bin/python3
def uppercase(str):
    for c in str:
        word = ord(c)
        if word >= 97 and word <= 122:
            word = chr(word - 32)
            print("{}".format(word), end='')
print("")
