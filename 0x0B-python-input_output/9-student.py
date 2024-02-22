#!/usr/bin/python3
"""
This module contains one class
"""


class Student:
    """
    a class Student that defines a student by:
    first_name
    last_name
    age
    """

    def __init__(self, first_name, last_name, age):
        """
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns the dictionary description
        with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        """
        return self.__dict__
