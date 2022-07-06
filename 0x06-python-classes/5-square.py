#!/usr/bin/python3
"""Module for creating a class for a square"""


class Square:
    """Class that defines a square

    Private instance attribute: size.

    Instantiation with optional size: def __init__(self, size=0).

    Public instance method: def area(self):
    that returns the current square area.

    Public instance method: def my_print(self):
    that prints in stdout the square with the character #.
    """
    def __init__(self, size=0):
        """Init method for the square class"""
        self.size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square to stdout"""
        if self.size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
