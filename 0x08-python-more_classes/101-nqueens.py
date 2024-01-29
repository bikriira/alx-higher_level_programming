#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at the given position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it's safe to place a queen at the given position,
            False otherwise.
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col):
    """
    Solve the N queens problem recursively using backtracking.

    Args:
        board (list): The current state of the chessboard.
        col (int): The current column being processed.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0

    return res


def print_solution(board):
    """
    Print a solution for the N queens problem.

    Args:
        board (list): The current state of the chessboard.
    """
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print(f"[{i}, {j}]", end=" ")
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: nqueens N\n")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            sys.stderr.write("N must be at least 4\n")
            sys.exit(1)
    except ValueError:
        sys.stderr.write("N must be a number\n")
        sys.exit(1)

    # Initialize the board
    board = [[0] * N for _ in range(N)]

    solve_n_queens(board, 0)
