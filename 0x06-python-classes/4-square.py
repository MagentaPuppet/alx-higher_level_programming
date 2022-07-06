#!/usr/bin/python3
"""Module for creating a class for a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Init method for the square class"""
        self.__ispositiveint(size)
        self.__size = size
        self.size = size

    def __ispositiveint(self, value):
        if not type(value) == int:
            raise TypeError("size must be in integer")
        if not value >= 0:
            raise ValueError("size must be >= 0")
        return True

    def area(self):
        self.__ispositiveint(self.size)
        return self.size ** 2

    def size(self):
        self.__ispositiveint(self.size)
        return self.size

    def size(self, value):
        self.__ispositiveint(value)
        self.size = value
