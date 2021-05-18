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
        choice_index = self.restrict_input_int(f"What's your choice?")
        while choice_index < 0 or choice_index >= len(self.choices):
            print("Invalid Input! Please try again!")
            choice_index = self.restrict_input_int(f"What's your choice?")
        self.choice = self.choices[choice_index]

    def restrict_input_int(self, prompt):
        while True:
            try:
                result = int(input(prompt))
                return result
            except ValueError as e:
                print("Invalid input! Enter a number")
