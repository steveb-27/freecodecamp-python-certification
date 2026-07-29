from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    @abstractmethod
    def level_up(self):
        pass

    def make_move(self):
        """Adds a move to a random position"""
        move = random.choice(self.moves)
        position = tuple(sum(x) for x in zip(move, self.position))
        self.position = position
        self.path.append(position)
        return move


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0,1),
            (0,-1),
            (-1,0),
            (1,0)
        ]

    def level_up(self):
        self.moves += [
            (1,1),
            (1,-1),
            (-1,1),
            (-1,-1)
        ]
