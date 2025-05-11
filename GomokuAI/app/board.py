from typing import List, Dict
import numpy as np
from app.player import Player

class Board:
    def __init__(self, board_size=9):
        self.board_size = board_size
        self.board = np.zeros((self.board_size, self.board_size), dtype=int)
        self.current_player = Player.Black
        return
    
    def reset(self):
        raise NotImplementedError

    
    
    def make_move(self, x: int, y: int):
        if self.board[x, y] != 0:
            raise ValueError
        self.board[x, y] = self.current_player.value
        self.current_player = Player.switch_player(self.current_player)
        return
    
    def undo_move(self, x: int, y: int):
        self.board[x, y] = 0
        self.current_player = Player.switch_player(self.current_player)
        raise
    
    def get_current_state(self):
        raise NotImplementedError
    
    def get_legal_moves(self):
        raise NotImplementedError
    
    def is_full(self):
        raise NotImplementedError