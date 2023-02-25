import random
from constants import BOARD_SIZE, EMPTY_CELL
from custom_types import Move



def display_welcome_message() -> None:
    print('*' * 10, 'Welcome to Tic-Tac-Toe game!', '*' * 10)


def get_player_name() -> str:
    name = input('Please input your name: ')
    print(f'Hi, {name}! Let`s play!')
    return name


def display_board(board: list[list[str]]) -> None:
    for row in range(BOARD_SIZE):
        print(EMPTY_CELL + " | ".join(board[row]) + EMPTY_CELL)
        if row != BOARD_SIZE - 1:
            print("----" * BOARD_SIZE)


def initialize_board() -> list[list[str]]:
   return [[EMPTY_CELL for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]


def is_valid_move(board: list[list[str]], row: int, col: int) -> bool:
    return not (row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE) and board[row][col] == EMPTY_CELL


def check_win(board: list[list[str]], size: int) -> str:
    for coord in range(size):
        if all(board[coord][i] == board[coord][0] and board[coord][0] != EMPTY_CELL for i in range(size)):
            return board[coord][0]
        if all(board[i][coord] == board[0][coord] and board[0][coord] != EMPTY_CELL for i in range(size)):
            return board[0][coord]
    if all(board[i][i] == board[0][0] and board[0][0] != EMPTY_CELL for i in range(size)):
        return board[0][0]
    if all(board[i][size-i-1] == board[0][size-1] and board[0][size-1] != EMPTY_CELL for i in range(size)):
        return board[0][size-1]
    return EMPTY_CELL


def try_move(board: list[list[str]], row: int, col: int, symbol: str) -> bool:
    if board[row][col] != EMPTY_CELL:
        return False
    board[row][col] = symbol
    return True


def find_potential_win_move(board: list[list[str]], computer_symbol: str) -> tuple[int, int] | None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if try_move(board, row, col, computer_symbol):
                if try_move(board, row, col, computer_symbol) and check_win(board, BOARD_SIZE) == computer_symbol:
                    return row, col
                board[row][col] = EMPTY_CELL
    return None


def find_random_move(board: list[list[str]]) -> tuple[int, int] | None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(board, row, col):
                return row, col

    return None


def get_computer_move(board: list[list[str]], computer_symbol: str) -> tuple[int, int] | None:
    move = find_potential_win_move(board, computer_symbol)
    if move:
        return move

    random_move = find_random_move(board)
    return random_move

    return None


def get_player_move(board: list[list[str]], symbol: str, player_name: str, board_size: int) -> Move:
    row = int(input(f'Please enter row number, {player_name} (0 - {board_size - 1}):  '))
    col = int(input(f'Please enter col number, {player_name} (0 - {board_size - 1}):  '))
    return Move(row=row, col=col)


def take_turns(board: list[list[str]], symbols: list[str], player_name: str, player_symbol: str, computer_symbol: str) -> str | None:
    winner = EMPTY_CELL
    while winner == EMPTY_CELL:
        display_board(board)
        if player_symbol == symbols[0]:
            player_move = get_player_move(board, player_symbol, player_name, BOARD_SIZE)
            if is_valid_move(board, player_move.row, player_move.col):
                board[player_move.row][player_move.col] = symbols[1]
                player_symbol, computer_symbol = computer_symbol, player_symbol
            else:
                print("Oh, it is invalid move, try again please")
                continue
        else:
            move = get_computer_move(board, computer_symbol=computer_symbol)
            if move is not None:
                row, col = move
                board[row][col] = computer_symbol
                player_symbol, computer_symbol = computer_symbol, player_symbol
            else:
                print("It's a tie!")
                break
        winner = check_win(board, BOARD_SIZE)
    display_board(board)
    announce_winner(winner)


def announce_winner(winner: str | None) -> None:
    if winner is not None:
        print(f'Game over, congratulations {winner}!')
    else:
        print("It's a tie!")


def tic_tac_toe_game() -> None:
    display_welcome_message()
    player_name = get_player_name()
    board = initialize_board()
    symbols = ['X', 'O']
    player_symbol = random.choice(symbols)
    computer_symbol = symbols[0] if player_symbol == symbols[1] else symbols[1]
    take_turns(board, symbols, player_name, player_symbol, computer_symbol)


if __name__ == '__main__':
    tic_tac_toe_game()
