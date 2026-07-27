from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        """Adds a move to a random position"""

    @abstractmethod
    def level_up(self):
        """"""


class Pawn(Player):
    def __init__(self):
        super().__init__()

    def level_up(self):
        """"""
