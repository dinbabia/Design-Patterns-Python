
from game_interface import IGame
from leaderboard_singleton import Leaderboard

class Game2(IGame):

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)


