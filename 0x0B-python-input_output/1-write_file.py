#!/usr/bin/python3
"""
This module contains one function
"""


def read_file(filename=""):
    """ reads a text file and prints its content """
    with open(filename) as file:
        return len(file)
