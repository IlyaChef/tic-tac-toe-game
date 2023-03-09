from constants import BOARD_SIZE, SYMBOL_TO_STRING
from custom_types import Symbol


def display_welcome_message() -> None:
    print('*' * 10, 'Welcome to Tic-Tac-Toe game!', '*' * 10)


def get_player_name() -> str:
    name = input('Please input your name: ')
    print(f'Hi, {name}! Let`s play!')
    return name


def display_board(board: list[list[str]]) -> None:
    for row in range(BOARD_SIZE):
        print(Symbol.EMPTY.value + " | ".join(SYMBOL_TO_STRING.get(symbol, str(symbol)) for symbol in board[row]) + Symbol.EMPTY.value)  # type: ignore
        if row != BOARD_SIZE - 1:
            print("----" * BOARD_SIZE)
