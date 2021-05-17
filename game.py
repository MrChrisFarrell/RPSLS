from player import Player
from computer_player import ComputerPlayer


class Game:
    def __init__(self):
        self.player1 = Player("")
        self.player2 = Player("")
        self.rounds = 3
        self.win = 2
        self.players = 1
        self.welcome_message = f"\nWelcome to Rock, Paper, Scissors, Lizard, Spock"

    def run_game(self):
        self.display_centered(self.welcome_message, 50)
        self.display_centered(f"This game will be best of {self.rounds}", 47)
        self.players_select()
        self.player1.select()
        self.player2.select()
        self.throw()
        #player selects choice
        #compare choices
        #display winner/draw of round
        #loop until set win number
        #display winner
        #play again?
        pass

    def players_select(self):
        self.players = int(input("\nEnter the number of players (max 2):"))
        while self.players <1 or self.players > 2:
            print("Invalid Input")
            self.players = int(input("Enter the number of players (max 2):"))
        if self.players == 2:
            self.player1.name = input("Enter Player-One name:")
            self.player2.name = input("Enter Player-Two name:")
        else:
            self.player1.name = input("Enter Player-One name:")
            self.player2 = ComputerPlayer()
        print(f"\n{self.player1.name} is going against {self.player2.name}")

    def display_centered(self, message, display_width):
        print(message.center(display_width))

    def throw(self):
        print(f"{self.player1.name} throws {self.player1.choice.name}. {self.player2.name} throws {self.player2.choice.name}")
        self.player1.choice.compare(self.player2.choice)
        self.player2.choice.compare(self.player1.choice)
        if self.player1.choice.win:
            self.player1.points += 1
            print(f"{self.player1.name} wins! Awarded 1 point.\nTotal points: {self.player1.points}")
        elif self.player2.choice.win:
            self.player2.points += 1
            print(f"{self.player2.name} wins! Awarded 1 point.\nTotal points: {self.player2.points}")
        else:
            print("The result is a: Draw! No points!")
        self.player1.choice.win = False
        self.player2.choice.win = False
