#!/usr/bin/python3
"""Module to divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix by div
    and return the result as a new matrix
    Args:
        matrix (list): matrix to divide its elements by div
        (list of lists of integers or floats)
        div (int or float): number to divide the matrix by
        (div != 0) (integer or float)
    Returns:
        list: new matrix with the result of the division of each
        element of matrix by div (list of lists of integers or floats)
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if div is not an integer or float
        TypeError: if matrix contains rows of different sizes
        ZeroDivisionError: if div is equal to 0
    """
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
