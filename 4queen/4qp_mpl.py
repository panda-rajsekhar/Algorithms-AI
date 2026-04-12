import matplotlib.pyplot as plt
import numpy as np

# Function to display the board using matplotlib
def plot_board(board):
    n = len(board)
    fig, ax = plt.subplots()

    # Create chessboard pattern
    chessboard = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            chessboard[i][j] = (i + j) % 2

    ax.imshow(chessboard)

    # Add queens
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ax.text(j, i, '♛', ha='center', va='center', fontsize=40)

    # Remove ticks
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()


# Safety check function
def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False

    return True


# Backtracking solver
def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False


# Main function
def four_queens():
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens(board, 0):
        plot_board(board)
    else:
        print("Solution does not exist.")


# Run
four_queens()
