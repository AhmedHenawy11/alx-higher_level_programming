#!/usr/bin/python3
"""
This module contains one class Square that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string representation of an object """
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)
