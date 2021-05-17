from player import Player


class Game:
    def __init__(self):
        self.player1 = Player("")
        self.player2 = Player("")
        self.rounds = 3
        self.players = 1
        self.welcome_message = f"\nWelcome to Rock, Paper, Scissors, Lizard, Spock"

    def run_game(self):
        self.display_centered(self.welcome_message, 50)
        self.display_centered(f"This game will be best of {self.rounds}", 47)
        self.players_select()
        print(self.players)
        #Have player(s) enter name(s)
        #player selects choice
        #compare choices
        #display winner/draw of round
        #loop until set win number
        #display winner
        #play again?
        pass

    def players_select(self):
        self.players = int(input("Enter the number of players (max 2)"))
        while self.players <1 or self.players > 2:
            print("Invalid Input")
            self.players = int(input("Enter the number of players (max 2)"))

    def display_centered(self, message, display_width):
        print(message.center(display_width))
