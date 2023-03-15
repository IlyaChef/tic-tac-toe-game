import pytest
from game_logic import initialize_board, is_valid_move, check_win, try_move, get_potential_win_move, find_random_move, take_turns
from constants import BOARD_SIZE
from custom_types import Symbol


def test_initialize_board():
    board = initialize_board()
    assert len(board) == 4
    assert all(len(row) == 4 for row in board)


@pytest.mark.parametrize(
    "row, col, expected",
    [
        (0, 0, True),
        (0, 1, True),
        (1, 1, True),
        (2, 2, True),
        (3, 3, True),
        (-2, 0, False),
        (0, -3, False),
        (4, 0, False),
        (0, 4, False),
    ]
)
def test_is_valid_move(empty_board, row, col, expected):
    assert is_valid_move(empty_board, row, col) == expected


def test_check_win():
    board = [
        [Symbol.O.value, Symbol.O.value, Symbol.EMPTY.value, Symbol.EMPTY.value],
        [Symbol.X.value, Symbol.O.value, Symbol.X.value, Symbol.EMPTY.value],
        [Symbol.EMPTY.value, Symbol.X.value, Symbol.O.value, Symbol.EMPTY.value],
        [Symbol.EMPTY.value, Symbol.X.value, Symbol.EMPTY.value, Symbol.O.value],
    ]
    assert check_win(board, BOARD_SIZE) == Symbol.O.value


def test_try_move(empty_board):
    assert not try_move(empty_board, 0, 0, 'O')
    assert not try_move(empty_board, 0, 0, 'X')


def test_get_potential_win_move():
    board = [
        [Symbol.X, Symbol.O, Symbol.EMPTY, Symbol.EMPTY],
        [Symbol.O, Symbol.X, Symbol.O, Symbol.EMPTY],
        [Symbol.EMPTY, Symbol.EMPTY, Symbol.X, Symbol.EMPTY],
        [Symbol.EMPTY, Symbol.EMPTY, Symbol.EMPTY, Symbol.EMPTY]]
    assert get_potential_win_move(board, Symbol.X) == (3, 3)


def test_find_random_move():
    board = [
        [Symbol.O.value, Symbol.X.value, Symbol.EMPTY.value, Symbol.O.value],
        [Symbol.X.value, Symbol.O.value, Symbol.X.value, Symbol.EMPTY.value],
        [Symbol.EMPTY.value, Symbol.EMPTY.value, Symbol.EMPTY.value, Symbol.X.value],
        [Symbol.O.value, Symbol.X.value, Symbol.EMPTY.value, Symbol.O.value],
    ]
    assert find_random_move(board) in [(0, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 2)]


def test__take_turns__player_symbol_wins():
    board = [
        [Symbol.O.value, Symbol.X.value, Symbol.EMPTY.value, Symbol.EMPTY.value],
        [Symbol.O.value, Symbol.X.value, Symbol.X.value, Symbol.EMPTY.value],
        [Symbol.O.value, Symbol.EMPTY.value, Symbol.EMPTY.value, Symbol.X.value],
        [Symbol.O.value, Symbol.EMPTY.value, Symbol.EMPTY.value, Symbol.EMPTY.value],
    ]
    symbols = ['X', 'O']
    player_name = 'Ilya'
    player_symbol = 'O'
    computer_symbol = 'X'

    winner = take_turns(board, symbols, player_name, player_symbol, computer_symbol)
    assert winner == player_symbol


def test_announce_winner():
    winner = Symbol.X.value
    assert f'Game over, congratulations {winner}!'
