from selection_list import SelectionList


class Player:
    def __init__(self, name):
        self.name = name
        self.choices = SelectionList().list
        self.choice = None
        self.points = 0

    def select(self):
        print(f"\n{self.name}, select what to throw!")
        choice_index = 0
        for choice in self.choices:
            print(f"Enter {choice_index} for {choice.name}")
            choice_index += 1
        choice_index = int(input(f"What's your choice?"))
        self.choice = self.choices[choice_index]


