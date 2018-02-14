import random

# Each one gets added one extra number for the range(1, gameNumbs*) *no inclusive.
POWERBALL, POWERPLAY = 70, 27 #e.g.(POWERBALL uses 69 numbers.)
GOPHER5 = 48
NORTHSTAR = 32
LOTTOAMERICA, LOTAMEPOWERPLAY = 53, 11
MEGAMILLIONS, MEGABALL = 71, 26
LUCKYFORLIFE, LUCKYBALL = 49, 19

# Number of times won with 3, 4, etc.
ONE_NUMB, TWO_NUMBS, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS, SIX_NUMBS = 0, 0, 0, 0, 0, 0

COUNTER = 0
QUIT_PICK_FIVE = set()
QUIT_PICK_ONE = set()

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
    print("\tIt took {:.2f} years to win with \t*{}* numbers!"\
                "\n{}   <--Your numbers"\
                "\n{}   <--Comp numbers"\
                "\n{}   <--Matching numbers".format(*fiveNumbs))

def _wins_six_numbs_games(*sixNumbs):
    print("\tIt took {:.2f} years to win with \t*{}* numbers!"\
                "\n{} {}   <--Your numbers"\
                "\n{} {}   <--Comp numbers"\
                "\n{} {}   <--Matching numbers".format(*sixNumbs))

def display_results(years, name):
    print("\tHere are the numbers of times each match ocurred for"\
    "\n {} year/s for {}"\
    "\nThere were {} times with 1 numbers."\
    "\nThere were {} times with 2 numbers."\
    "\nThere were {} times with 3 numbers."\
    "\nThere were {} times with 4 numbers."\
    "\nThere were {} times with 5 numbers."\
    .format(years, name, ONE_NUMB, TWO_NUMBS, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS))

    if name == "Powerball" or name == "MegaMillions" or name == "LuckyForLife" or name == "LottoAmerica":
        print("There were {} times with 6 numbers.".format(SIX_NUMBS))

def comp_draws(name, numbOfPicks, numbOfDays, drawFive, timesAWeek, drawOne=None):
    global ONE_NUMB, TWO_NUMBS, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS, SIX_NUMBS,\
           QUIT_PICK_FIVE, QUIT_PICK_ONE, COUNTER, totalFourOrMore

    if numbOfPicks == 0: # This is for the qpicks that are only drawn once for the time of the program.
        numbOfPicks = numbOfDays
    numbOfMatches = 0
    thisNumbOfPicks = numbOfPicks # thisNumbOfPicks var will change and want to keep the original intact.

    print("\n\nWins with 4 or more numbers! for {}".format(name))

    for numb in range(numbOfDays // numbOfPicks): # Fo the quick picks only.
        QUIT_PICK_FIVE = _pick_five(drawFive)
        if drawOne != None:
            QUIT_PICK_ONE = _pick_one(drawOne)

        drawsWeekly = (thisNumbOfPicks // 7) * timesAWeek # To be used with the inner loop only.

        for x in range(drawsWeekly):
            draws = _pick_five(drawFive)
            all_numbs = list(draws) # Save a list for printing.
            # Check and see if there are matching numbers and keep trak or print.
            draws &= QUIT_PICK_FIVE # kee only the matching numbes <set &= other>.

            if drawOne != None:
                draw_one = _pick_one(drawOne)
                quick_one = list(draw_one)
                draw_one &= QUIT_PICK_ONE # See if it matches.
                numbOfMatches = len(draws) + len(draw_one)

                if numbOfMatches == 1: ONE_NUMB += 1
                elif numbOfMatches == 2: TWO_NUMBS += 1
                elif numbOfMatches == 3: THREE_NUMBS += 1
                if numbOfMatches > 3:
                    totalFourOrMore += 1
                    if len(draw_one) == 0:
                        draw_one = 0
                    elif numbOfMatches == 4:
                        FOUR_NUMBS += 1
                        _wins_six_numbs_games((COUNTER/365), numbOfMatches, sorted(QUIT_PICK_FIVE),\
                         QUIT_PICK_ONE, sorted(all_numbs), quick_one, sorted(draws), draw_one)
                    elif numbOfMatches == 5:
                        FIVE_NUMBS += 1
                        _wins_six_numbs_games((COUNTER/365), numbOfMatches, sorted(QUIT_PICK_FIVE),\
                         QUIT_PICK_ONE,sorted(all_numbs), quick_one, sorted(draws), draw_one)
                    elif numbOfMatches == 6:
                        SIX_NUMBS += 1
                        _wins_six_numbs_games((COUNTER/365), numbOfMatches, sorted(QUIT_PICK_FIVE),\
                        QUIT_PICK_ONE, sorted(all_numbs), quick_one, sorted(draws), draw_one)

            else:
                numbOfMatches = len(draws)
                if numbOfMatches > 3: totalFourOrMore += 1
                if numbOfMatches == 1: ONE_NUMB += 1
                elif numbOfMatches == 2: TWO_NUMBS += 1
                elif numbOfMatches == 3: THREE_NUMBS += 1
                elif numbOfMatches == 3:
                    THREE_NUMBS += 1
                elif numbOfMatches == 4:
                    FOUR_NUMBS += 1
                    _wins_five_numbs_games((COUNTER/365), numbOfMatches, sorted(QUIT_PICK_FIVE), sorted(all_numbs), sorted(draws))
                elif numbOfMatches == 5:
                    THREE_NUMBS += 1
                    _wins_five_numbs_games((COUNTER/365), numbOfMatches, sorted(QUIT_PICK_FIVE), sorted(all_numbs), sorted(draws))

            COUNTER += 1

        # The reason for getting the remainder is important, let's say that a user wants his quick picks
        # to be drawn every 30 days, the math is that 30 // 7(to get a whole numb) = 4 and have 2 left.
        # In a year, there will be 14 days no draws, (4 missed in a twice a week game or more), data will not be acurate.
        if thisNumbOfPicks % 7 == 1:
            thisNumbOfPicks = numbOfPicks
        else:
            thisNumbOfPicks += (thisNumbOfPicks % 7)

    if FOUR_NUMBS == 0 and FIVE_NUMBS == 0 and SIX_NUMBS == 0:
        print("***No wins with 4 numbers or more.***")

    display_results(int(numbOfDays/365), name)

    ONE_NUMB, TWO_NUMBS, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS, SIX_NUMBS = 0, 0, 0, 0, 0, 0
    COUNTER, QUIT_PICK_FIVE, QUIT_PICK_ONE = 0, 0, 0
