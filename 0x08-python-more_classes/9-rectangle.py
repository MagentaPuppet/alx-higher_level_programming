#!/usr/bin/python3
"""Module for class Rectangle"""


class Rectangle:
    """Class that defines a rectangle

    Private instance attribute: width

    Private instance attribute: height

    Public class attribute: number_of_instances

    Public class attribute: print_symbol

    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):

    Public instance method: def area(self):
    that returns the rectangle area

    Public instance method: def perimeter(self):
    that returns the rectangle perimeter

    print() and str() should print the rectangle with the character #

    repr() should return a string representation of the rectangle
    to be able to recreate a new instance by using eval()

    Print the message Bye rectangle... (... being 3 dots not ellipsis)
    when an instance of Rectangle is deleted
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init method for the class Rectangle"""
        self.height = height
        self.width = width
        self.number_of_instances += 1

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
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """returns the string representation of the rectangle
        to be able to create a new instance by using eval()
        """
        return "{}({}, {})".format(
          type(self).__name__, self.__width, self.__height)

    def __del__(self):
        """prints the message "Bye rectangle..." when
        an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        self.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method that returns the bigger rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area()) == (rect_2.area()) or \
           (rect_1.area()) >= (rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that returns a new Rectangle instance
        with width == height == size
        """
        return cls(size, size)
