import random
import sys


# Setting up a player object to use
class Player:
    def __init__(self, name):
        self.name = name


class Game:

    def __init__(self, player):
        self.player = player

    # Setting up the main game  logic
    @staticmethod
    def play():
        move_set = ['rock', 'paper', 'scissors']
        c_move = random.choice(move_set)
        p_move = input('Please enter rock, paper, or scissors.')

        # Player wins
        if (p_move, c_move) == ('rock', 'scissors'):
            print('Player wins!')
        elif (p_move, c_move) == ('scissors', 'paper'):
            print('Player wins!')
        elif (p_move, c_move) == ('paper', 'rock'):
            print('Player wins!')
        # Computer wins
        elif (p_move, c_move) == ('rock', 'paper'):
            print('Computer wins!')
        elif (p_move, c_move) == ('paper', 'scissors'):
            print('Computer wins!')
        elif (p_move, c_move) == ('scissors', 'rock'):
            print('Computer wins!')
        # If both moves are the same it's a tie game
        elif p_move == c_move:
            print('It\'s a tie!')

    # Setting up the game loop
    def game_loop(self):
        while True:
            print('Welcome to Rock, Paper, Scissors!')
            # If user enters something outside the move set list
            self.play()
            # After each round the user is asked whether they want to continue
            if not self.play_again():
                print('Thanks for playing!')
                break
        sys.exit()

    # Setting up the play again logic
    @staticmethod
    def play_again():
        p_answer = input('Would you like to play again?(Enter yes or no)')
        p_answer = p_answer.strip()
        p_answer = p_answer.lower()
        if p_answer == 'n' or p_answer == 'no':
            return False
        return True


player_1 = Player('George')
game_1 = Game(player_1)
game_1.game_loop()
