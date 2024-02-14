#!/usr/bin/python3
"""
Module 2-rectangle
"""


class Rectangle:
    """
    Defines class rectangle private attribute width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__ (self, width, height)
        width (self)
        width (self, value)
        height (self)
        height (self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initialize  rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets height-if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method returns area"""
        return self.area

    def perimeter(self):
        """Method returns perimeter"""
        if self.height == 0 or self.width == 0:
            self.perimeter = 0
        return self.perimeter

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        ch = ''
        if self.__width == 0 or self.__height == 0:
            return ch
        for i in range(self.height):
            for i in  range(self.width):
                ch += "#"
            ch += '\n'
        return ch[:-1]
