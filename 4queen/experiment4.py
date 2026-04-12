import matplotlib.pyplot as plt
import numpy as np

# Function to display the board
def plot_board(board, title="Solution"):
    n = len(board)
    fig, ax = plt.subplots()

    chessboard = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            chessboard[i][j] = (i + j) % 2

    ax.imshow(chessboard)

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                ax.text(j, i, '♛', ha='center', va='center', fontsize=30)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)

    plt.show()


# Safety check
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


# Modified solver to store ALL solutions
def solve_n_queens(board, row, solutions):
    if row == len(board):
        # Deep copy the solution
        solutions.append([r[:] for r in board])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_n_queens(board, row + 1, solutions)
            board[row][col] = 0   # backtrack


# Main function
def four_queens():
    n = 4
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, solutions)

    print(f"Total solutions: {len(solutions)}")

    for i, sol in enumerate(solutions):
        plot_board(sol, title=f"Solution {i+1}")


# Run
four_queens()
