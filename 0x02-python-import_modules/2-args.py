#!/usr/bin/python3
if __name__ == "__main__":
    import sys
num1 = len(sys.argv) - 1
if num1 == 0:
    print("{} argument.".format(num1))
elif num1 == 1:
    print("{} argument:".format(num1))
    for i in range(1, num1 + 1):
        print("{}: {}".format(i, sys.argv[i]))
else:
    print("{} argument:".format(num1))
    for j in range(1, num1 + 1):
        print("{}: {}".format(j, sys.argv[j]))

