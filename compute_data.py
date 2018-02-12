import random
from try_your_luck_game_app import GAMES_CHOSEN

# Each one gets added one extra number for the range(1, gameNumbs*) *no inclusive.
POWERBALL, POWERPLAY = 70, 27 #e.g.(POWERBALL uses 69 numbers.)
GOPHER5 = 48
NORTHSTAR = 32
LOTTOAMERICA, LOTAMEPOWERPLAY = 53, 11
MEGAMILLIONS, MEGAPLAY = 71, 26

# Number of times won with 3, 4, etc.
THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS, SIX_NUMBS = 0, 0, 0, 0

COUNTER = 0
QUIT_PICK_FIVE = set()
QUIT_PICK_ONE = set()

def _pick_five(game):
    # Get five numbers from the numbers in a game e.g. Northstar 1-31 add one to 31 for inclusive.
    # set is working good in this case, but I think list also works.
    return set(random.sample(range(1, game), 5))

def _pick_one(game):
    return set(random.sample(range(1, game), 1))

def winnings_print(*args):
    print("It took {:.2f} years to match $$$$$$ {} numbers \n{} <- Your numbers \
    \n{} <- Computer numbers \n{} Matched \n".format(*args))

def print_results():
    if FOUR_NUMBS == 0 and FIVE_NUMBS == 0:
        print("Sorry!! No winnings! with 4 numbers or more.")

        print("\n{} times with 3 numbers.\n{} times with 4 numbers.\n{} times with five"\
        .format(THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS))

def comp_draws(numbOfPicks, gameChosen, gameName = None):
    global QUIT_PICK_FIVE, COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS

    for x in range(numbOfPicks):
        draws = _pick_five(gameChosen)
        match = list(draws) # Save a list for printing.
        draws &= QUIT_PICK_FIVE # kee only the matching numbes <set &= other>.
        # Check and see if there are matching numbers and keep trak or print.
        if gameChosen == "Powerball" or gameChosen == "MegaMillions":
            draw_one = _pick_one(gameChosen)
            draw_one &= QUIT_PICK_ONE
            if len(draws) + len(draw_one) == 3:
                THREE_NUMBS += 1
            elif len(draws) + len(draw_one) == 4:
                FOUR_NUMBS += 1
                winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), QUIT_PICK_ONE, sorted(match), sorted(draws))
            elif len(draws) + len(draw_one) == 5:
                FIVE_NUMBS += 1
                winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), QUIT_PICK_ONE, sorted(match), sorted(draws))
                COUNTER += 1
            elif len(draws) + len(draw_one) == 6:
                SIX_NUMBS += 1
                winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), QUIT_PICK_ONE, sorted(match), sorted(draws))
                COUNTER += 1

        else:
            if len(draws) == 3:
                THREE_NUMBS += 1
            elif len(draws) == 4:
                FOUR_NUMBS += 1
                winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), sorted(match), sorted(draws))
            elif len(draws) == 5:
                THREE_NUMBS += 1
                winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), sorted(match), sorted(draws))
                COUNTER += 1

def results_northstar(numbYears, numbQPicks):
    # If the player choose one quick pick only once for the number of years, the outter loop will
    # only loop once. Northstar plays everyday.
    global QUIT_PICK_FIVE
    if numbQPicks == 0: # Using the same numbers for the number of years.
        QUIT_PICK_FIVE = _pick_five(NORTHSTAR) # quick pick for user.
        print("\n*Your Northstar numbers!*"\
             "\nOnly the winnings with 4 or more numbers were shown.\n")
        numbQPicks = numbYears
        comp_draws(numbQPicks, NORTHSTAR)

    else:
        print("\nYour Northstar numbers!")
        for n in range(numbYears//numbQPicks):
            QUIT_PICK_FIVE = _pick_five(NORTHSTAR)

            # function to get the draws and check them against the quik pick numbers.
            comp_draws(numbQPicks, NORTHSTAR)

    print("\n*Your Northstar numbers!*")
    print_results()
    global COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS
    QUIT_PICK_FIVE, COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS = 0, 0, 0, 0, 0

def results_powerball(numbOfQuickPicks):
    # Powerball only plays twice in a week, so number of draws is 2.
    # If the player choose one quick pick only once for the number of years, the outter loop will
    # only loop once. Northstar plays everyday.

    global COUNTER, QUIT_PICK_FIVE, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS

    if numbQPicks == 0: # Using the same numbers for the number of years.
        QUIT_PICK_FIVE = _pick_five(POWERBALL) # quick pick for user.
        QUIT_PICK_ONE = _pick_one(POWERPLAY)
        print("\n*Your Northstar numbers!*"\
             "\nOnly the winnings with 4 or more numbers were shown.\n")
        numbQPicks = numbYears
        comp_draws(numbQPicks, NORTHSTAR)

    else:
        print("\nYour Northstar numbers!")
        for n in range(numbYears//numbQPicks):
            QUIT_PICK_FIVE = _pick_five(NORTHSTAR)

            # function to get the draws and check them against the quik pick numbers.
            comp_draws(numbQPicks, NORTHSTAR)

    print("\n*Your Northstar numbers!*")
    print_results()
    COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS = 0, 0, 0, 0
