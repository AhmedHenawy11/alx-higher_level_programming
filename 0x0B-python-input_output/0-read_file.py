#!/usr/bin/python3

def read_file(filename=""):
    """
    function that print the content of file
    :param filename: a file to be passed and print its outpu
    """
    with open(filename, 'r') as file:
        print(file.read())
