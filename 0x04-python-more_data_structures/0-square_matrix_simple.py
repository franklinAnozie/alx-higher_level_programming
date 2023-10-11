#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(matrix[i].copy())
        for j in range(len(matrix[i])):
            new_matrix[i][j] = new_matrix[i][j] ** 2

    return new_matrix


if __name__ == "__main__":
    square_matrix_simple()
