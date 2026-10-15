# Tic-Tac-Toe Game

board = [" " for _ in range(9)]


def display_board():
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
                board[position[1]] == player and
                board[position[2]] == player):
            return True

    return False


def board_full():
    return " " not in board


def play_game():
    current_player = "X"

    print("TIC-TAC-TOE")
    print("Positions are:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:
        display_board()

        try:
            position = int(input(
                f"Player {current_player}, enter position (1-9): "
            ))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("That position is already occupied.")
                continue

            board[position - 1] = current_player

            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break

            if board_full():
                display_board()
                print("It's a draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    play_game()
