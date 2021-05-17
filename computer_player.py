import random

from player import Player


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Robot")

    def select(self):
        self.choice = random.randint(0, len(self.choices) - 1)
