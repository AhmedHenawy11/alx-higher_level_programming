#!/usr/bin/python3
"""
This module contains one function
"""


def write_file(filename="", text=""):
    """ appends  a text into file and return ist length , and creates the file if it doesn't exist"""
    with open(filename, 'a') as file:
        return file.write(text)
