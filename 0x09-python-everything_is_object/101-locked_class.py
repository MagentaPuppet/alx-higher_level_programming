#!/usr/bin/python3
"""Module for creating a locked class"""


class LockedClass:
    """Class that only allows attributes with the name first_name"""
    __slots__ = ['first_name']

    def __init__(self):
        pass
