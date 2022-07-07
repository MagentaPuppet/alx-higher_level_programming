#!/usr/bin/python3
"""Module that contains a function for dividing a matrix"""


def matrix_divided(matrix, div):
    """Functions that divides all elements of a matrix"""
    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) != list:
        raise TypeError(
          "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) != list:
            raise TypeError(
              "matrix must be a matrix (list of lists) of integers/floats")

    for i in range(len(matrix)):
        if i > 0:
            if len(matrix[i - 1]) != len(matrix[i]):
                raise TypeError(
                  "Each row of the matrix must have the same size")

        new_matrix += [[]]
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")

            new_matrix[i] += [round(j/div, 2)]
    return new_matrix
