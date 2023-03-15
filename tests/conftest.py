import pytest
from game_logic import initialize_board


@pytest.fixture
def empty_board():
    return initialize_board()
