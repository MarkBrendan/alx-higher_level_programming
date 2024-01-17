#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            str_pass = chr(ord(i) - 32)
            print("{}".format(str_pass), end=" ")
        else:
            print("{}".format(i), end=" ")
