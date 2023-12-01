#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    sum = 0
    for num in argv:
        if num != argv[0]:
            sum += int(num)
    print(sum)
