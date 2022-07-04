#!/usr/bin/python3
"""Module for creating a class for a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Init method for the square class"""
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if not size >= 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
