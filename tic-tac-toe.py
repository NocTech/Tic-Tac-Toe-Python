def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Function to check if the specified player has won
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # Function to check if the board is full (a draw)
    return all(cell != " " for row in board for cell in row)

def main():
    # Initialize the game board and current player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)  # Display the current state of the board
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter the row (0, 1, 2): "))  # Get the row input from the current player
            col = int(input("Enter the column (0, 1, 2): "))  # Get the column input from the current player

            if row < 0 or row > 2 or col < 0 or col > 2:
                # Check for invalid inputs (out of range)
                print("Invalid input. Row and column must be between 0 and 2.")
                continue

            if board[row][col] == " ":
                # Check if the selected position is empty
                board[row][col] = current_player  # Place the player's symbol on the board
            else:
                print("That position is already taken. Try again.")
                continue
        except ValueError:
            # Handle non-integer inputs
            print("Invalid input. Please enter a valid number.")
            continue

        if check_winner(board, current_player):
            # Check if the current player has won
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break

        if is_board_full(board):
            # Check if the board is full (a draw)
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"  # Switch to the other player

if __name__ == "__main__":
    main()
