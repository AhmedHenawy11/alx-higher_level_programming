#!/usr/bin/python3
"""
This module contains one function
"""


def read_file(filename=""):
    """
    function that print the content of file
    :param filename: a file to be passed and print its outpu
    """
    with open(filename) as file:
        for line in file:
            print(line, end="")
