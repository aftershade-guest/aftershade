def is_winner(player_list):
    for case in WIN_CASES:
        if len([n for n in case if n in player_list]) == 3:
            return True

# def inp_ceh():
#    in_ = input("Enter cells: ").upper()
#    if len(in_) > 9:
#        print("Input is too long")
#        inp_ceh()
#    else:
#        global in_str
#        in_str = in_


def check_board(coordinate):
    if board[coordinate] == '_':
        return True
    else:
        return False


def print_board():
    print(f"""---------
    | {board[0]} {board[1]} {board[2]} |
    | {board[3]} {board[4]} {board[5]} |
    | {board[6]} {board[7]} {board[8]} |
    ---------""")


def check_game():
    global GameFinished
    xs = [i for i, n in enumerate(board) if n == "X"]
    os = [i for i, n in enumerate(board) if n == "O"]

    if is_winner(xs) and is_winner(os) or abs(len(xs) - len(os)) > 1:
        GameFinished = True
        print("Impossible")

    else:
        if is_winner(xs):
            GameFinished = True
            print("X wins")
        elif is_winner(os):
            GameFinished = True
            print("O wins")
        elif "_" in board:
            GameFinished = False
            print("Game not finished")
        else:
            GameFinished = True
            print("Draw")


def input_coord():
    rerun = False
    in_co = input("Enter the coordinates: ").split()
    in_co = "".join(in_co)
    if in_co.isnumeric():
        for i in range(len(in_co)):
            if in_co[i] in not_all:
                rerun = True

        if rerun:
            print("Coordinate should be from 1 to 3!")
            return None
        else:
            return in_co
    else:
        print("You should enter numbers")
        input_coord()


def game_():
    global player
    in_coord = input_coord()

    if in_coord is None:
        in_coord = input_coord()

    coord_index = 0

    for i, u in enumerate(board_cord):
        if u == in_coord:
            coord_index = i

    if check_board(coord_index):
        board[coord_index] = Mark
        print_board()
        check_game()
        player += 1
    else:
        print("This cell is occupied! Choose another one")
        game_()


player = 1
GameFinished = False
board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

print_board()

WIN_CASES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

not_all = ["0", "4", "5", "6", "7", "8", "9"]
board_cord = ["11", "12", "13", "21", "22", "23", "31", "32", "33"]

while not GameFinished:

    if player % 2 != 0:
        print("Player X's turn")
        Mark = "X"
    else:
        print("Player O's turn")
        Mark = "O"
    game_()
