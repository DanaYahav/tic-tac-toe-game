import random


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_win(board, symbol):

    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == symbol and \
           board[condition[1]] == symbol and \
           board[condition[2]] == symbol:
            return True

    return False


def get_move(board, player_name, symbol):

    while True:

        try:
            move = int(input(f"{player_name} ({symbol}) choose position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position. Choose 1-9.")
                continue

            if board[move] != " ":
                print("This place is already taken! Try again.")
                continue

            board[move] = symbol
            break

        except ValueError:
            print("Invalid input! Please enter a number.")


def computer_move(board, symbol):

    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = symbol


def play_game():

    board = [" "] * 9

    mode = input("Choose mode: 1 = Player vs Player, 2 = Player vs Computer: ")

    player1 = input("Enter name for Player 1: ")

    if mode == "2":
        player2 = "Computer"
    else:
        player2 = input("Enter name for Player 2: ")

    symbol = input(f"{player1}, choose X or O (press Enter for random): ")

    if symbol == "":
        symbol = random.choice(["X","O"])

    symbol = symbol.upper()

    if symbol == "X":
        symbol1 = "X"
        symbol2 = "O"
    else:
        symbol1 = "O"
        symbol2 = "X"

    current_player = player1
    current_symbol = symbol1

    while True:

        print_board(board)

        if current_player == "Computer":
            computer_move(board, current_symbol)
        else:
            get_move(board, current_player, current_symbol)

        if check_win(board, current_symbol):

            print_board(board)
            print(f"{current_player} wins!")
            break

        if " " not in board:

            print_board(board)
            print("It's a tie!")
            break

        if current_player == player1:
            current_player = player2
            current_symbol = symbol2
        else:
            current_player = player1
            current_symbol = symbol1


while True:

    play_game()

    again = input("Do you want to play again? (y/n): ")

    if again.lower() != "y":
        print("Thanks for playing!")
        break

if __name__ == "__main__":
    main()