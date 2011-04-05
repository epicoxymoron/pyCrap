from game import Bet

BIG_6 = Bet(
    "Big 6", 
	lambda d: sum(d) == 6,
	lambda d: sum(d) == 7,
	1,
	5.0 / 36
)

BIG_8 = Bet(
    "Big 8", 
	lambda d: sum(d) == 8,
	lambda d: sum(d) == 7,
	1,
	5.0 / 36
)

HARD_4 = Bet(
    "Hard Way 4",
    lambda d: d == [2, 2],
    lambda d: (sum(d) == 7 or (sum(d) == 4 and d != [2, 2])),
    7,
    None
)

HARD_6 = Bet(
    "Hard Way 6",
    lambda d: d == [3, 3],
    lambda d: (sum(d) == 7 or (sum(d) == 6 and d != [3, 3])),
    9,
    None
)

HARD_8 = Bet(
    "Hard Way 8",
    lambda d: d == [4, 4],
    lambda d: (sum(d) == 7 or (sum(d) == 8 and d != [4, 4])),
    9,
    None
)

HARD_10 = Bet(
    "Hard Way 10",
    lambda d: d == [5, 5],
    lambda d: (sum(d) == 7 or (sum(d) == 10 and d != [5, 5])),
    7,
    None
)

bets_list = [BIG_6, BIG_8, HARD_4, HARD_6, HARD_8, HARD_10]
bets_dict = {}
for b in bets_list:
    bets_dict[b.name] = b
