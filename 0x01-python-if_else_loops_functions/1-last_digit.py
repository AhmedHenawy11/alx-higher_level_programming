#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    k = -1 * (- number % 10)
else:
    k = number % 10

if k > 5:
    print(f"Last digit of {number} is {k} and is greater than 5")
elif k == 0:
    print(f"Last digit of {number} is {k} and is 0")
elif k < 6 and k != 0:
    print(f"Last digit of {number} is {k}", end=" ")
    print(f"and is less than 6 and not 0")
