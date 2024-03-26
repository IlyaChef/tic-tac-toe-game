# Console Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game in Python.

## Overview

This project consists of the following files, directories, and configuration files:

- **game_logic.py**: Contains the game logic, including functions for initializing the board, making moves, checking for a winner, and managing turns between the player and the computer.

- **user_interface.py**: Provides functions for user interaction.

- **custom_types.py**: Defines custom data types used in the game. 

- **constants.py**: Contains game constants. You can customize the size of the game board by changing the BOARD_SIZE constant. By default, the board size is set to 4.
- **tictactoe.py**: The main script to run the Tic-Tac-Toe game.
- **requirements.txt**: Lists the Python dependencies required for running the project.
- **tests/**: Directory containing test scripts for the project.
- **setup.cfg**: Configuration file for Flake8 linter, specifying maximum line length, ignored error codes, and excluded directories.

## How to Play

1. Install the required dependencies by running the command:

```python
pip install -r requirements.txt
```

2. Run the `tictactoe.py` script:

```python
python3 tictactoe.py
```
   
3. Follow the prompts to input your name and make moves on the game board.

4. The computer will automatically make its moves after yours.

5. Continue taking turns until one player wins or the game ends in a draw.

## Requirements

- Python 3.x
