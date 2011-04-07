# Copyright 2011 Justin Williamson
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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

