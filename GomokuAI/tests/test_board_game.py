import pytest
import numpy as np
from app.board import Board
from app.player import Player


def test_board_initialization():
    # Test that a new board is empty and current_player is 1
    game_board = Board(board_size=9)
    assert np.all(game_board.board == 0)
    assert game_board.current_player == Player.Black

def test_make_move_and_switch_player():
    # Test making a move updates the board and switches current player
    game_board = Board(board_size=9)
    game_board.make_move(2, 3)
    assert game_board.board[2, 3] == Player.Black
    assert game_board.current_player == Player.White

def test_illegal_move_raises_exception():
    # Test that making a move in an occupied cell raises ValueError
    game_board = Board(board_size=9)
    game_board.make_move(4, 4)
    with pytest.raises(ValueError):
        game_board.make_move(4, 4)

def test_undo_move():
    # Test that undoing a move clears the cell and restores player
    game_board = Board(board_size=9)
    game_board.make_move(5, 5)
    game_board.undo_move(5, 5)
    assert game_board.board[5, 5] == 0
    assert game_board.current_player == Player.Black

def test_get_legal_moves():
    # Test that get_legal_moves returns correct empty positions
    game_board = Board(board_size=5)
    game_board.make_move(0, 0)
    legal_moves = game_board.get_legal_moves()
    assert (0, 0) not in legal_moves
    assert (0, 1) in legal_moves
    assert len(legal_moves) == 24

def test_get_current_state_tensor_shape():
    # Test that board state tensor has correct shape and values
    game_board = Board(board_size=9)
    game_board.make_move(1, 1)  # current_player Black → White
    game_board.make_move(2, 2)  # current_player White → Black
    tensor = game_board.get_current_state()
    assert tensor.shape == (2, 9, 9)
    # Tensor[0] == positions for current player
    assert tensor[0][2][2] == 1.0
    assert tensor[1][1][1] == 1.0