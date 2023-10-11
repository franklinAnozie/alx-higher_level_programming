#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [matrix[i].copy() for i in range(len(matrix))]
    new_matrix = [new_matrix[i][j] ** 2 for i in range(len(new_matrix))
                  for j in range(len(new_matrix[i]))]

    return new_matrix


if __name__ == "__main__":
    square_matrix_simple()
