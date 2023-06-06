#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 96 < ord(c) < 123 :
            c = chr(ord(c) - 32)
        print(f"{c}", end="")
    print("")
