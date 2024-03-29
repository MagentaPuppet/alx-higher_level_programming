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

    print() and str() should print the rectangle with the character #
    """
    def __init__(self, width=0, height=0):
        """init method for the class Rectangle"""
        self.width = width
        self.height = height

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

    def __str__(self):
        """gives the string representation of the rectangle"""
        string = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                string += "\n"
        return string[:-1]
