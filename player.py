from selection_list import SelectionList


class Player:
    def __init__(self, name):
        self.name = name
        self.choices = SelectionList().list
        self.choice = None
        self.points = 0

    def select(self):
        print("Select your choice")
        choice_index = 0
        for choice in self.choices:
            print(f"Enter {choice_index} for {choice}")
            choice_index += 1
        self.choice = int(input(f"What's your choice?"))

    def throw(self, enemy):
        print(f"{self.name} throws {self.choices[self.choice].name}. {enemy.name} throws {enemy.choices[enemy.choice].name}")
        self.choices[self.choice].compare(enemy.choices[enemy.choice].name)
        if self.choices[self.choice].win:
            self.points += 1
