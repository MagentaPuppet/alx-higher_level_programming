#!/usr/bin/python3
"""Module that contains a function for adding two numbers"""


def add_integer(a, b=98):
    """Functions that adds two numbers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    result = a + b
    return result
