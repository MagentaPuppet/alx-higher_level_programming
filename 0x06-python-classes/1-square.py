#!/usr/bin/python3
"""Module for creating a class for a square"""


class Square:
    """Class that defines a square"""
    def __init__(self, size):
        """Init method for the square class"""
        self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
