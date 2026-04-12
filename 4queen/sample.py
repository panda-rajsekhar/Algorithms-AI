# 4 queen problem in ai 
# Function to print the board configuration
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

# Function to check if a queen can be placed on board[row][col]
# This function checks the column and both diagonals
def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False

    return True

# Backtracking function to solve the problem
def solve_n_queens(board, row):
    # If all queens are placed, return True
    if row == len(board):
        return True

    # Try placing the queen in each column of the current row
    for col in range(len(board)):
        # Check if it's safe to place a queen at board[row][col]
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen

            # Recur to place the queen in the next row
            if solve_n_queens(board, row + 1):
                return True

            # Backtrack if placing queen in board[row][col] doesn't lead to a solution
            board[row][col] = 0

    # If no place is found, return False
    return False

# Function to solve the N Queens problem
def four_queens():
    n = 4  # Number of queens
    board = [[0 for _ in range(n)] for _ in range(n)]  # Initialize the board
    
    # Start the backtracking algorithm from the first row
    if solve_n_queens(board, 0):
        print_board(board)
    else:
        print("Solution does not exist.")

# Run the function
four_queens()
