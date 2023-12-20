#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square and its size and limiting size options."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print # of square num."""
        if self.size == 0:
            print("")
        else:
            for line in range(self.size):
                for n in range(self.size):
                    print("#", end="")
                print("")
