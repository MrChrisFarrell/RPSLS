from choice import Choice


class Paper(Choice):
    def __init__(self):
        super().__init__("Paper")

    def compare(self, opp_choice):
        if opp_choice.name == "Rock" or opp_choice.name == "Spock":
            self.win = True
        else:
            self.win = False

