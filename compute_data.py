import random
import try_your_luck_game_app
from try_your_luck_game_app import GAMES_CHOSEN

# Each one gets added one extra number for the range(1, gameNumbs*) *no inclusive.
POWERBALL, POWERPLAY = 70, 27 #(POWERBALL = 69 + 1)
GOPHER5 = 48
NORTHSTAR = 32
LOTTOAMERICA, LOTAMEPOWERPLAY = 53, 11
MEGAMILLIONS, MEGAPLAY = 71, 26

def compute_games_chosen(numbOfYears, gamesChosen):
    if 'Northstar' in gamesChosen:
        _numbOfQuickPicks = (numbOfYears * 365) // 7
        results_northstar(NORTHSTAR, _numbOfQuickPicks)

    # for game in gamesChosen: # list of games chosen by user.
    #     if game == 'Northstar': # if in list.

def results_northstar(game, numbOfQuickPicks):
    # Northstar draws are everyday, the program has to draw 7 times for each numbOfQuickPicks.
    northstar3, northstar4, northstar5 = 0, 0, 0
    numb = 0
    while numb <= numbOfQuickPicks:
        numb += 1 # Week 1

        # set is working good in this case, but I think list also works.
        quick_pick = set(random.sample(range(1,NORTHSTAR), 5))

        for n in range(7):
            draws = set(random.sample(range(1, NORTHSTAR), 5))
            draws &= quick_pick
            if len(draws) == 3:
                northstar3 += 1
                print("Week number {}\n {}\n {} ***3".format(numb, sorted(quick_pick), sorted(draws)))
            if len(draws) == 4:
                northstar4 += 1
                print("Week number {}\n {}\n {} ****4".format(numb, sorted(quick_pick), sorted(draws)))
            if len(draws) == 5:
                northstar5 += 1
                print("Week number {}\n {}\n {} *****5".format(numb, sorted(quick_pick), sorted(draws)))

    print("\nNorthstar game wins in {:.0f} year: \nWith 3 numbers: {} \nWith 4 number: {}\
        \nWith 5 numbers: {}".format((numbOfQuickPicks*7/365), northstar3, northstar4, northstar5))
