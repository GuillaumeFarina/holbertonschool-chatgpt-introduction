def print_board(board):
    print("  0 | 1 | 2")
    print("  ---------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)}")
        print("  ---------")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    if all(board[i][j] != " " for i in range(3) for j in range(3)):
        print("It's a tie!")
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input or spot already taken! Try again.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        board[row][col] = player
        player = "O" if player == "X" else "X"

    print_board(board)
    if not check_winner(board):
        print("Player " + player + " wins!")

tic_tac_toe()