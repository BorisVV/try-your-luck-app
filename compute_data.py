import random

# Each one gets added one extra number for the range(1, gameNumbs*) *no inclusive.
POWERBALL, POWERPLAY = 70, 27 #e.g.(POWERBALL uses 69 numbers.)
GOPHER5 = 48
NORTHSTAR = 32
LOTTOAMERICA, LOTAMEPOWERPLAY = 53, 11
MEGAMILLIONS, MEGABALL = 71, 26
LUCKYFORLIFE, LUCKYBALL = 49, 19

# game_choices = {
#     "Power Ball": 70,
#     "Power Play": 27,
#     "Gopher Five": 48,
#     "North Star": 32,
#     "Lotto America": 53,
#     "Star Ball": 11,
#     "Mega Millions": 71,
#     "Mega Ball": 26,
#     "Lucky For Life": 49,
#     "Lucky Ball": 19,
#     }

# matches with one number or more...
match_one_numb, match_two_numbs, match_three_numbs, match_four_numbs, match_five_numbs, match_six_numbs = 0, 0, 0, 0, 0, 0

counter = 0
quick_pick_five = set()
quick_pick_one = set()

totalFourOrMore = 0

def totalFourOrPlus():
    if totalFourOrMore > 0:
        print("\nTHERE WERE {} WINS!! WITH 4 OR MORE NUMBERS!".format(totalFourOrMore))
    else:
        print("\nNOT WININGS WITH 4 OR NUMBERS.")

def _pick_five(game):
    # Get five numbers from the numbers in a game e.g. Northstar 1-31 add one to 31 for inclusive.
    # set is working good in this case, but I think list also works.
    return set(random.sample(range(1, game), 5))

def _pick_one(game):
    return set(random.sample(range(1, game), 1))

def _wins_five_numbs_games(*fiveNumbs):
    print("  It took {:.2f} years to win with \t***** {} numbers!"\
                "\n\t{}   <--Your numbers"\
                "\n\t{}   <--Comp numbers"\
                "\n\t{}   <--Matching numbers".format(*fiveNumbs))

def _wins_six_numbs_games(*sixNumbs):
    print("  It took {:.2f} years to win with \t****** {} numbers!"\
                "\n\t{} {}   <--Your numbers"\
                "\n\t{} {}   <--Comp numbers"\
                "\n\t{} {}   <--Matching numbers".format(*sixNumbs))

def display_results(years, name):
    print("  Here are the numbers of times each match ocurred for"\
    "\n  {} year/s for {}"\
    "\nThere were {} times with 1 numbers."\
    "\nThere were {} times with 2 numbers."\
    "\nThere were {} times with 3 numbers."\
    "\nThere were {} times with 4 numbers."\
    "\nThere were {} times with 5 numbers."\
    .format(years, name, match_one_numb, match_two_numbs, match_three_numbs, match_four_numbs, match_five_numbs))

    if name == "Powerball" or name == "MegaMillions" or name == "LuckyForLife" or name == "LottoAmerica":
        print("There were {} times with 6 numbers.".format(match_six_numbs))

# def wins_six_numbs_games(*args):
#     _wins_six_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five),\
#         quick_pick_one,sorted(all_numbs), quick_one, sorted(draws), draw_one)
#     return match_five_numbs += 1

def comp_draws(name, numbOfPicks, numbOfDays, drawFive, timesAWeek, drawOne=None):
    global match_one_numb, match_two_numbs, match_three_numbs, match_four_numbs, match_five_numbs, match_six_numbs,\
           quick_pick_five, quick_pick_one, counter, totalFourOrMore

    if numbOfPicks == 1: # This is for the qpicks that are only drawn once for the time of the program.
        numbOfPicks = numbOfDays
        if "Northstar" == name: timesAWeek = numbOfDays
        else: timesAWeek = (numbOfPicks // 7) // timesAWeek # TODO: add comments next lines.
    elif numbOfPicks == 7: timesAWeek
    elif numbOfPicks == 14: timesAWeek *= 2
    elif numbOfPicks == 21: timesAWeek *= 3
    else: timesAWeek *= 4

    numbOfMatches = 0
    thisCounter = 0

    print("\nWins with 4 or more numbers! for {}".format(name))

    for qpick in range(numbOfDays // numbOfPicks): # For the quick picks only.
        quick_pick_five = _pick_five(drawFive)
        if drawOne != None:
            quick_pick_one = _pick_one(drawOne)

        for x in range(timesAWeek):
            draws = _pick_five(drawFive)
            all_numbs = list(draws) # Save a list for printing.
            # Check and see if there are matching numbers and keep trak or print.
            draws &= quick_pick_five # kee only the matching numbes <set &= other>.

            if drawOne != None:
                draw_one = _pick_one(drawOne)
                quick_one = list(draw_one)
                draw_one &= quick_pick_one # See if it matches.
                numbOfMatches = len(draws) + len(draw_one)

                if numbOfMatches == 1: match_one_numb += 1
                elif numbOfMatches == 2: match_two_numbs += 1
                elif numbOfMatches == 3: match_three_numbs += 1

                elif numbOfMatches > 3:
                    totalFourOrMore += 1

                    if len(draw_one) == 0:
                        draw_one = 0

                    if numbOfMatches == 4:
                        _wins_six_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five),\
                            quick_pick_one, sorted(all_numbs), quick_one, sorted(draws), draw_one)
                        match_four_numbs += 1

                    elif numbOfMatches == 5:
                        print("$" * 60) # TODO: remove add to a var to store result.
                        _wins_six_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five),\
                            quick_pick_one,sorted(all_numbs), quick_one, sorted(draws), draw_one)
                        match_five_numbs += 1
                        print("$" * 60) # TODO: remove

                    else:
                        print("$" * 60) # TODO: remove
                        _wins_match_six_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five),\
                            quick_pick_one, sorted(all_numbs), quick_one, sorted(draws), draw_one)
                        match_six_numbs += 1
                        print("$" * 60) # TODO: remove

            else:
                numbOfMatches = len(draws)

                if numbOfMatches == 1: match_one_numb += 1
                elif numbOfMatches == 2: match_two_numbs += 1
                elif numbOfMatches == 3: match_three_numbs += 1
                elif numbOfMatches > 3:
                    totalFourOrMore += 1

                    if numbOfMatches == 4:
                        _wins_five_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five), sorted(all_numbs), sorted(draws))
                        match_four_numbs += 1

                    else:
                        print("$" * 60) # TODO: remove
                        _wins_five_numbs_games((counter/365), numbOfMatches, sorted(quick_pick_five), sorted(all_numbs), sorted(draws))
                        match_five_numbs += 1
                        print("$" * 60) # TODO: remove

            counter += 1

    if match_four_numbs == 0 and match_five_numbs == 0 and match_six_numbs == 0:
        print("#No wins with 4 numbers or more.#")

    display_results(int(numbOfDays/365), name)

    match_one_numb, match_two_numbs, match_three_numbs, match_four_numbs, match_five_numbs, match_six_numbs = 0, 0, 0, 0, 0, 0
    counter, quick_pick_five, quick_pick_one = 0, 0, 0
