#!/usr/bin/python3

def matrix_divided(matrix, div):
    error = ["matrix must be a matrix (list of lists) of integers/floats",
             "div must be a number",
             "Each row of the matrix must have the same size",
             "division by zero"
             ]
    if not isinstance(matrix, list):
        raise TypeError(error[0])
    if not isinstance(div, (int, float)):
        raise TypeError(error[1])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(error[0])
        if len(matrix[0]) != len(i):
            raise TypeError(error[2])
        for j in range(len(i)):
            if not isinstance(i[j], (int, float)):
                raise TypeError(error[0])
    if div == 0:
        raise ZeroDivisionError(error[3])
    new_matrix = list(map(lambda x: x.copy(), matrix))
    new_matrix = list(map(lambda row:
                          list(map(lambda x, div: x / div, row,
                                   [div] * len(row))), new_matrix))
    return new_matrix


if __name__ == "__main__":
    matrix_divided()
