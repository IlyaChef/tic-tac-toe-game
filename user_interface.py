from constants import BOARD_SIZE
from custom_types import Symbol
from typing import Union


def display_welcome_message() -> None:
    print('*' * 10, 'Welcome to Tic-Tac-Toe game!', '*' * 10)


def get_player_name() -> str:
    name = input('Please input your name: ')
    print(f'Hi, {name}! Let`s play!')
    return name


def display_board(board: list[list[Union[Symbol, str]]]) -> None:
    for row in range(BOARD_SIZE):
        print(Symbol.EMPTY.value + " | ".join(str(symbol) for symbol in board[row]) + Symbol.EMPTY.value)
        if row != BOARD_SIZE - 1:
            print("----" * BOARD_SIZE)
