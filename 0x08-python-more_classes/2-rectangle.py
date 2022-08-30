#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    """Class that defines a rectangle

    Private instance attribute: width

    Private instance attribute: height

    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):

    Public instance method: def area(self):
    that returns the rectangle area

    Public instance method: def perimeter(self):
    that returns the rectangle perimeter
    """
    def __init__(self, width=0, height=0):
        """init method for the class Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle's area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)
