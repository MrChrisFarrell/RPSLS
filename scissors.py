from choice import Choice


class Scissors(Choice):
    def __init__(self):
        super().__init__("Scissors")

    def compare(self, opp_choice):
        if opp_choice.name == "Paper" or opp_choice.name == "Lizard":
            self.win = True
        else:
            self.win = False

