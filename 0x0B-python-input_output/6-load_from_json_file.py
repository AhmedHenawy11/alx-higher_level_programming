#!/usr/bin/python3
"""
This module contains one function
"""
import json


def load_from_json_file(filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'r') as file:
        return file.write(json.loads(file.read()))
