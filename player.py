from selection_list import SelectionList


class Player:
    def __init__(self, name):
        self.name = name
        self.choices = SelectionList().list
        self.choice = None

    def select(self):
        print("Select your choice")
        choice_index = 0
        for choice in self.choices:
            print(f"Enter {choice_index} for {choice}")
            choice_index += 1
        self.choice = int(input(f"What's your choice?"))
