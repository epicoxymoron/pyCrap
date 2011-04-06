"""Basic game logic classes"""

from collections import deque
from logging import Logger
from random import randint
from config import config

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
    
    def __repr__(self):
        return self.name

class Bet(object):
    """A place on the table where a player can make a bet"""
    
    def __init__(self, name, desc, fwin, flose, payout, odds, **kwargs):
        self.name = name
        self.description = desc
        self.win = fwin
        self.lose = flose
        self.payout = payout
        self.odds = odds

    def __repr__(self):
        return "{0}: {1}".format(self.name, self.description)

class Game(object):
    """A game of Craps"""

    STATE_OFF = "OFF"
    STATE_ON = "ON"
    BET_LIST = [
        Bet("Big 6", (
            "This bet wins when a dice roll totals 6, and loses when a " + 
            "dice roll totals 7.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: sum(d) == 6,
            lambda d: sum(d) == 7,
            1, 5 / 36
        ),
        Bet("Big 8", (
            "This bet wins when a dice roll totals 8, and loses when a " + 
            "dice roll totals 7.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: sum(d) == 8,
            lambda d: sum(d) == 7,
            1, 5 / 36
        ),
        Bet("Hard Way 4", (
            "This bet wins when the dice a pair of 2s is rolled, and " +
            "loses when any other combination totalling 4 (an \"easy way " +
            "4\") or 7 is rolled.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: d == [2, 2],
            lambda d: (sum(d) == 7 or (sum(d) == 4 and d != [2, 2])),
            7, None
        ),
        Bet("Hard Way 6", (
            "This bet wins when the dice a pair of 3s is rolled, and " +
            "loses when any other combination totalling 6 (an \"easy way " +
            "6\") or 7 is rolled.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: d == [3, 3],
            lambda d: (sum(d) == 7 or (sum(d) == 6 and d != [3, 3])),
            9, None
        ),
        Bet("Hard Way 8", (
            "This bet wins when the dice a pair of 4s is rolled, and " +
            "loses when any other combination totalling 8 (an \"easy way " +
            "8\") or 7 is rolled.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: d == [4, 4],
            lambda d: (sum(d) == 7 or (sum(d) == 8 and d != [4, 4])),
            9, None
        ),
        Bet("Hard Way 10", (
            "This bet wins when the dice a pair of 5s is rolled, and " +
            "loses when any other combination totalling 10 (an \"easy way " +
            "10\") or 7 is rolled.  Any other roll keeps this bet on the " +
            "table."),
            lambda d: d == [5, 5],
            lambda d: (sum(d) == 7 or (sum(d) == 10 and d != [5, 5])),
            7, None
        )
    ]

    def __init__(self):
        self.players = deque()
        self.state = "OFF"
        self.logger = Logger()
        self.roll_history = []
        self.dice = Dice()

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

    def shoot_dice(self):
        self.dice.roll()

    def rotate_shooters(self):
        self.players.rotate(-1)
        self.bets = []
        self.roll_history = []
    
class Wager(object):
    def __init__(self, player, bet):
        self.player = player
        self.bet = bet

