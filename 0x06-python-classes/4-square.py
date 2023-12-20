#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square and its size and limiting size options."""
    def __init__(self, size=0):
        self.size = size

    def size(self):
        return (self.__size)

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
