from choice import Choice


class Spock(Choice):
    def __init__(self):
        super().__init__("Spock")

    def compare(self, opp_choice):
        if opp_choice.name == "Scissors" or opp_choice.name == "Rock":
            self.win = True
        else:
            self.win = False

