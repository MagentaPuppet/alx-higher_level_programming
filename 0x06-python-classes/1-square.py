#!/usr/bin/python3
"""Module for creating a class for a square"""


class Square:
    """Class that defines a square
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """Init method for the square class"""
        self.__size = size
