#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    l = 0
    r = 0
    for list in matrix:
        new_matrix.append(list)
    for ls in matrix:
        r = 0
        for i in ls:
            new_matrix[l][r] = pow(i, 2)
            r += 1
        l += 1
    return new_matrix
