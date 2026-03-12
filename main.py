import random

def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_win(board, s):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == s:
            return True
    return False


def get_move(board, name, symbol):
    while True:
        try:
            pos = int(input(f"{name} ({symbol}) choose 1-9: ")) - 1

            if pos < 0 or pos > 8:
                print("Choose a number between 1-9")
                continue

            if board[pos] != " ":
                print("Place already taken!")
                continue

            board[pos] = symbol
            break

        except:
            print("Invalid input")


def play_game():

    board = [" "] * 9

    p1 = input("Player 1 name: ")
    p2 = input("Player 2 name: ")

    sym = input(f"{p1} choose X or O (Enter=random): ")

    if sym == "":
        sym = random.choice(["X","O"])

    sym = sym.upper()

    if sym == "X":
        s1, s2 = "X","O"
    else:
        s1, s2 = "O","X"

    player = p1
    symbol = s1

    while True:

        print_board(board)

        get_move(board, player, symbol)

        if check_win(board, symbol):
            print_board(board)
            print(player,"wins!")
            break

        if " " not in board:
            print_board(board)
            print("Tie!")
            break

        if player == p1:
            player = p2
            symbol = s2
        else:
            player = p1
            symbol = s1


while True:

    play_game()

    again = input("Play again? y/n: ")

    if again.lower() != "y":
        break

if __name__ == "__main__":
    main()

