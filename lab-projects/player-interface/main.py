from abc import ABC

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]