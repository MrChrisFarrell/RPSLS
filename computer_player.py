import random

from player import Player


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Kevin Costner")

    def select(self):
        choice_index = random.randint(0, len(self.choices) - 1)
        self.choice = self.choices[choice_index]
