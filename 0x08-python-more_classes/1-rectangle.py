#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """init method for the class Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """returns the width of the rectangle"""
        pass

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
        pass

    @height.setter
    def height(self, value):
        """setter for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
