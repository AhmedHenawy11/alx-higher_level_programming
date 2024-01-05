#!/usr/bin/python3

"""Making private attributes height and width"""


class Rectangle:
    """
    Defining a  class rectangle private attributes width and height
    Attributes:
        width (int): width
        height (int): height
    Methods:
        __init__ (self, width, height)
        width (self)
        width (self, value)
        height (self)
        height (self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initialize  rectangles attributes"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Getter return width"""
        return self._width

    @width.setter
    def width(self, value):
        """Height Setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Getter return height"""
        return self._height

    @height.setter
    def height(self, value):
        """Height Setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
