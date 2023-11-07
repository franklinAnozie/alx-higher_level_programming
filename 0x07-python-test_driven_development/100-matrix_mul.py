#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    rowA = len(m_a)
    rowB = len(m_b)
    colA = len(m_a[0])
    colB = len(m_b[0])

    new_matrix1 = [[0] * colB for _ in range(rowA)]

    for i in range(rowA):
        for j in range(colB):
            for k in range(colA):
                new_matrix1[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix1


if __name__ == "__main__":
    a = [[1, 4], [2, 5], [3, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    print(matrix_mul(a, b))
