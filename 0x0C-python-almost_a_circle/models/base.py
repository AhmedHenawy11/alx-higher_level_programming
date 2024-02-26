#!/usr/bin/python3
"""
This module contains one class: Base
"""
import json
import csv


class Base:
    """
    The goal of this class is:
    to manage id attribute in all our future classes
    and to avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiation """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
