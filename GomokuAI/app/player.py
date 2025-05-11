from __future__ import annotations
from enum import Enum

class Player(Enum):
    Black = 1
    White = -1

    @staticmethod
    def switch_player(current_player: Player):
        if current_player == Player.Black:
            return Player.White
        else:
            return Player.Black

        