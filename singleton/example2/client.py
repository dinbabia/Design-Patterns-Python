from game1 import Game1
from game2 import Game2
from game3 import Game3

g1 = Game1()
g1.add_winner(2, "Din")

g2 = Game2()
g2.add_winner(1, "Alden")

g3 = Game3()
g3.add_winner(3, "Sol")

print("Game 1")
g1.leaderboard.print()
print("Game 2")
g2.leaderboard.print()
print("Game 3")
g3.leaderboard.print()




