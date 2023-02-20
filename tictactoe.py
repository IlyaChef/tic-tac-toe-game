import random
from constants import EMPTY_CELL


def welcome_message() -> None:
    print('*' * 10, 'Welcome to Tic-Tac-Toe game!', '*' * 10)


def get_player_name() -> str:
    name = input('Please input your name: ')
    print(f'Hi, {name}! Let`s play!')
    return name


def display_board(board: list[list[str]]) -> None:
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")


def initialize_board() -> list[list[str]]:
   return [[EMPTY_CELL for col in range(3)] for row in range(3)]


def is_valid_move(board: list[list[str]], row: int, col: int) -> bool:
    return not (row < 0 or row > 2 or col < 0 or col > 2) and board[row][col] == EMPTY_CELL


def check_win(board: list[list[str]]) -> str:
    for coord in range(3):
        if board[coord][0] == board[coord][1] == board[coord][2] and board[coord][0] != EMPTY_CELL:
            return board[coord][0]
        if board[0][coord] == board[1][coord] == board[2][coord] and board[0][coord] != EMPTY_CELL:
            return board[0][coord]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY_CELL:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY_CELL:
        return board[0][2]
    return EMPTY_CELL


def find_win_move(board: list[list[str]], computer_symbol: str) -> tuple[int, int]:
    for row in range(3):
        for col in range(3):
            if is_valid_move(board, row, col):
                board[row][col] = computer_symbol
                if check_win(board) == computer_symbol:
                    return row, col
                board[row][col] = EMPTY_CELL
    return None

def find_random_move(board: list[list[str]]) -> tuple[int, int]:
    for row in range(3):
        for col in range(3):
            if is_valid_move(board, row, col):
                return row, col

    return None

def get_computer_move(board: list[list[str]], computer_symbol: str) -> tuple[int, int]:
    move = find_win_move(board, computer_symbol)
    if move:
        return move

    return find_random_move(board)


def get_player_move(board: list[list[str]], symbol: str, player_name: str) -> dict:
    row = int(input(f'Please enter row number, {player_name} (0, 1, 2): '))
    col = int(input(f'Please enter col number, {player_name} (0, 1, 2): '))
    return {"row": row, "col": col}


def announce_winner(winner: str) -> None:
    if winner:
        print("{} won!".format(winner))
    else:
        print("It's a tie!")


def tic_tac_toe_game() -> None:
    welcome_message()
    player_name = get_player_name()
    board = initialize_board()
    symbols = ['X', 'O']
    player_symbol = random.choice(symbols)
    computer_symbol = symbols[0] if player_symbol == symbols[1] else symbols[1]
    winner = EMPTY_CELL
    while winner == EMPTY_CELL:
        display_board(board)
        if player_symbol == symbols[0]:
            player_move = get_player_move(board, player_symbol, player_name)
            if is_valid_move(board, player_move['row'], player_move['col']):
                board[player_move['row']][player_move['col']] = symbols[1]
                player_symbol, computer_symbol = computer_symbol, player_symbol
            else:
                print("Oh, it is invalid move, try again please")
                continue
        else:
            row, col = get_computer_move(board, computer_symbol=computer_symbol)
            board[row][col] = computer_symbol
            player_symbol, computer_symbol = computer_symbol, player_symbol
        winner = check_win(board)
    display_board(board)
    announce_winner(winner)



if __name__ == '__main__':
    tic_tac_toe_game()

