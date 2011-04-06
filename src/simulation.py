from game import *

game = Game()
game.add_player(Player("Alice"))
game.add_player(Player("Bob"))
game.add_player(Player("Eve"))
print("Players: {0}".format(game.players))

print("Bets:")
for b in game.BET_LIST:
    print("\t{0}".format(b))

game.shoot_dice()
print("Dice: {0}".format(game.dice.values()))

