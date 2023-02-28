import random
from user_interface import display_welcome_message, get_player_name
from game_logic import initialize_board, take_turns


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
