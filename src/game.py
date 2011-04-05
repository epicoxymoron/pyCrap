"""Basic game logic classes"""

from collections import deque
from logging import Logger
from random import randint

class Dice(object):
    """The dice that a shooter rolls"""

    def __init__(self):
        """Constructs a Dice instance and gives an initial roll.
        Once constructed, .values() will be in a usable state"""
        self.dice = self.roll()

    def roll(self):
        """Rolls the dice and returns the values"""
        self.dice = sorted([self._roll_die(), self._roll_die()])
        return self.values()

    def sum(self):
        """Gets the sum of the rolled dice"""
        return sum(self.dice)

    def values(self):
        """Gets the individual face values of the rolled dice"""
        return self.dice

    @staticmethod
    def _roll_die():
        """Rolls a single die"""
        return randint(1, 6)


class Player(object):
    """A player of the game"""

    def __init__(self, name, money=None):
        self.name = name
        self.bet_history = []
        if money is None:
            money = config.get("Players", "startingCash")
        self.money = money

class Game(object):
    """A game of Craps"""

    STATE_OFF = "OFF"
    STATE_ON = "ON"

    def __init__(self):
        self.players = deque()
        self.bets = []
        self.state = "OFF"
        self.logger = Logger()
        self.roll_history = []

    def add_player(self, player):
        """Adds a player next to the shooter"""
        self.players.append(player)

    def shooters_in_front(self, player):
        """Counts the number of shooters in front of a player"""
        position = 0
        for p in self.players():
            if p == player:
                return position
            else:
                position += 1
        return -1

    def current_shooter(self):
        """Gets the current shooter"""
        if len(self.players) > 0:
            return self.players[0]
        else:
            return None

    def rotate_shooters(self):
        self.players.rotate(-1)
        self.bets = []
        self.roll_history = []
    
class Bet(object):
    """A place on the table where a player can make a bet"""
    
    def __init__(self, name, fwin, flose, payout, odds, **kwargs):
        self.name = name
        self.win = fwin
        self.lose = flose
        self.payout = payout
        self.odds = odds

    def __repr__(self):
        pass

class Wager(object):
    def __init__(self, player, bet):
        self.player = player
        self.bet = bet

