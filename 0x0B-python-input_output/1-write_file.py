#!/usr/bin/python3
"""
This module contains one function
"""


def write_file(filename="", text=""):
    """ appends  a text into file and return ist length """
    with open(filename, 'w') as file:
        return file.write(text)
