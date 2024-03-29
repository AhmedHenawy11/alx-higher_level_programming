#!/usr/bin/python3
"""
This module contains one function
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w') as file:
        return file.write(json.dumps(my_obj))
