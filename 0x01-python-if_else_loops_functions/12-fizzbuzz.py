#!/usr/bin/python3
def fizzbuzz():
    o = "Fizz"
    p = "Buzz"
    q = "FizzBuzz"
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("{}".format(q), end=" ")
        elif i % 3 == 0:
            print("{}".format(o), end=" ")
        elif i % 5 == 0:
            print("{}".format(p), end=" ")
        else:
            print("{}".format(i), end=" ")
