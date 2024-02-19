#!/usr/bin/python3
"""
This module contains one function:

say_my_name(a, b)
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name function prints your name : first_name and last_name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string$')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string$')

    if last_name == "":
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
