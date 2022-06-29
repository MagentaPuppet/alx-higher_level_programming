#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_result = []
    for i in range(len(matrix)):
        matrix_result += [[]]
        for j in range(len(matrix[i])):
            matrix_result[i] += [matrix[i][j]**2]
    return matrix_result
