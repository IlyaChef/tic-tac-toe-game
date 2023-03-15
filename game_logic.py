from constants import BOARD_SIZE
from custom_types import Move, Symbol
from user_interface import display_board


def initialize_board() -> list[list[Symbol]]:
    return [[Symbol.EMPTY for col in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]


def is_valid_move(board: list[list[Symbol]], row: int, col: int) -> bool:
    return not (row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE) and board[row][col] == Symbol.EMPTY.value


def check_win(board: list[list[Symbol]], size: int) -> Symbol:
    for coord in range(size):
        if all(board[coord][i] == board[coord][0] and board[coord][0] != Symbol.EMPTY for i in range(size)):
            return board[coord][0]
        if all(board[i][coord] == board[0][coord] and board[0][coord] != Symbol.EMPTY for i in range(size)):
            return board[0][coord]
    if all(board[i][i] == board[0][0] and board[0][0] != Symbol.EMPTY for i in range(size)):
        return board[0][0]
    if all(board[i][size - i - 1] == board[0][size - 1] and board[0][size - 1] != Symbol.EMPTY for i in range(size)):
        return board[0][size - 1]
    return Symbol.EMPTY


def try_move(board: list[list[Symbol]], row: int, col: int, symbol: str) -> bool:
    if board[row][col] != Symbol.EMPTY:
        return False
    board[row][col] = symbol
    return True


def get_potential_win_move(board: list[list[Symbol]], computer_symbol: str) -> tuple[int, int] | None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            board_copy = [row[:] for row in board]
            if try_move(board_copy, row, col, computer_symbol) and check_win(board_copy, BOARD_SIZE) == Symbol(computer_symbol):
                return row, col
    return None


def find_random_move(board: list[list[Symbol]]) -> tuple[int, int] | None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(board, row, col):
                return row, col

    return None


def get_computer_move(board: list[list[Symbol]], computer_symbol: str) -> tuple[int, int] | None:
    move = get_potential_win_move(board, computer_symbol)
    if move:
        return move

    random_move = find_random_move(board)
    return random_move

    return None


def get_player_move(board: list[list[Symbol]], symbol: str, player_name: str, board_size: int) -> Move:
    row = int(input(f'Please enter row number, {player_name} (0 - {board_size - 1}):  '))
    col = int(input(f'Please enter col number, {player_name} (0 - {board_size - 1}):  '))
    return Move(row=row, col=col)


def take_turns(board: list[list[Symbol]], symbols: list[str], player_name: str, player_symbol: str, computer_symbol: str) -> Symbol | str:
    winner: Symbol | str = Symbol.EMPTY.value
    while winner == Symbol.EMPTY.value:
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
            move = get_computer_move(board, computer_symbol=Symbol(computer_symbol).value)
            if move is not None:
                row, col = move
                board[row][col] = Symbol(computer_symbol).value
                player_symbol, computer_symbol = computer_symbol, player_symbol
            else:
                print("It's a tie!")
                break
        winner = check_win(board, BOARD_SIZE)
    display_board(board)
    announce_winner(winner)
    return winner


def announce_winner(winner: Symbol | str) -> None:
    if winner is not None:
        print(f'Game over, congratulations {winner}!')
    else:
        print("It's a tie!")
