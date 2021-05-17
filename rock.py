from choice import Choice


class Rock(Choice):
    def __init__(self):
        super().__init__("Rock")

    def compare(self, opp_choice):
        if opp_choice.name == "Scissors" or opp_choice.name == "Lizard":
            self.win = True
        else:
            self.win = False
