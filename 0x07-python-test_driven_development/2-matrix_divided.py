#!/usr/bin/python3
"""
module contain function that divides all elements of a matrix
matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of matrix by div.
    Return the new matrix with the new divided values
    """
    row = len(matrix[0])
    print(row)
    for i in matrix:

        if len(i) != row:
            raise TypeError("Each row of the matrix must have the same size")
        if type(matrix) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in i:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    length = 0
    index = 0

    for li in matrix:
        divided_matrix.append(li)
        for i in li:
            i = round((i / div), 2)
            divided_matrix[length][index] = i
            index += 1
        index = 0
        length += 1

    return divided_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")