#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num1 = len(sys.argv) - 1
    if num1 == 0:
        print("0 arguments.")
    elif num1 == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num1))
    for j in range(1, num1 + 1):
        print("{:d}: {}".format(j, sys.argv[j]))
