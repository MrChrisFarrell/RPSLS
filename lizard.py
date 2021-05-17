from choice import Choice


class Lizard(Choice):
    def __init__(self):
        super().__init__("Lizard")

    def compare(self, opp_choice):
        if opp_choice.name == "Spock" or opp_choice.name == "Paper":
            self.win = True
        else:
            self.win = False

