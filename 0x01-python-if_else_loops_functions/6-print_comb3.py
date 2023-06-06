#!/usr/bin/python3
for digits in range(0, 10):
    for digit in range(digits + 1, 10):
        if digits == 8 and digit == 9:
            print("{}{}".format(digits, digit))
        else:
            print("{}{}".format(digits, digit), end=", ")
