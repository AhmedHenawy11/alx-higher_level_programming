#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    l = 0
    r = 0
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_matrix)
