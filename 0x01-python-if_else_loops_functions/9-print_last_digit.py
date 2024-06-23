#!/usr/bin/python3
def print_last_digit(number):
    last_dit = abs(number) % 10
    print(last_dit, end="")
    return last_dit
