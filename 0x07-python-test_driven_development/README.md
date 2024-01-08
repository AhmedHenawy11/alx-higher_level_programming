#Test Driven Developent and Unit Testing with Python

#Testing test file:
python3 -m doctest -v ./tests/file.txt

    for i in matrix[0]:
        list_1.append(round((i / div), 2))
        length_1 += 1
    for i in matrix[1]:
        list_2.append(round((i / div), 2))
        length_2 += 1

    if length_1 != length_2:
        raise TypeError("Each row of the matrix must have the same size")
    
    divided_matrix.append(list_1)