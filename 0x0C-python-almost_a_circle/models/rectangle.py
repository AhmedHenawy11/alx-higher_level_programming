#!/usr/bin/python3
"""
This module contain Rectangle class
"""
from base import Base


class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ return the area of the circle """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle in stdout with '#' """
        """ prints the rectangle in stdout with '#' """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """ string representation of the object """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
