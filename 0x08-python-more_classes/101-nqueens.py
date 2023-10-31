#!/usr/bin/python3
""" Module 101-nqueens """

from sys import argv


def nqueens(n):
    """ nqueens - finds all possible solutions to the N queens problem
    Arguments:
        n: size of the board
    Returns:
        list of solutions
    """
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for col in range(n)] for row in range(n)]
    solutions = []
    solve(board, 0, solutions)
    return solutions


def solve(board, col, solutions):
    """ solve - recursive function to find solutions
    Arguments:
        board: chessboard
        col: column to start checking from
        solutions: list of solutions
    """
    if col == len(board):
        add_solution(board, solutions)
        return
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, col + 1, solutions)
            board[row][col] = 0


def is_safe(board, row, col):
    """ is_safe - checks if a position is safe
    Arguments:
        board: chessboard
        row: row to check
        col: column to check
    Returns:
        True if safe, False otherwise
    """
    for c in range(col):
        if board[row][c] == 1:
            return False
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    for r, c in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    return True


def add_solution(board, solutions):
    """ add_solution - adds a solution to the solutions list
    Arguments:
        board: chessboard
        solutions: list of solutions
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    solutions.append(solution)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    solutions = nqueens(n)
    for sol in solutions:
        print(sol)
