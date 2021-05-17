from rock import Rock
from scissors import Scissors
from paper import Paper
from lizard import Lizard
from spock import Spock


class SelectionList:
    def __init__(self):
        rock = Rock()
        paper = Paper()
        scissors = Scissors()
        lizard = Lizard()
        spock = Spock()
        self.list = [rock, paper, scissors, lizard, spock]
