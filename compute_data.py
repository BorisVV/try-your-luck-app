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

def _pick_five(game):
    # Get five numbers from the numbers in a game e.g. Northstar 1-31 add one to 31 for inclusive.
    # set is working good in this case, but I think list also works.
    return set(random.sample(range(1, game), 5))

def results_northstar(numbYears, numbQPicks):
    # If the player choose one quick pick only once for the number of years, the outter loop will
    # only loop once. Northstar plays everyday.

    global COUNTER, QUIT_PICK_FIVE

    if numbQPicks == 0: # Using the same numbers for the number of years.
        QUIT_PICK_FIVE = _pick_five(NORTHSTAR) # quick pick for user.
        print("\nYour Northstar numbers!")
        numbQPicks = numbYears
        comp_draws(numbQPicks, NORTHSTAR)

    else:
        print("\nYour Northstar numbers!")
        for n in range(numbYears//numbQPicks):
            QUIT_PICK_FIVE = _pick_five(NORTHSTAR)

            # function to get the draws and check them against the quik pick numbers.
            comp_draws(numbQPicks, NORTHSTAR)



def comp_draws(numbOfPicks, gameChosen):
    global QUIT_PICK_FIVE, COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS
    for x in range(numbOfPicks):
        draws = _pick_five(gameChosen)
        match = list(draws) # Save a list for printing.
        draws &= QUIT_PICK_FIVE # kee only the matching numbes <set &= other>.
        # Check and see if there are matching numbers and keep trak or print.
        if len(draws) == 3:
            THREE_NUMBS += 1
        elif len(draws) == 4:
            FOUR_NUMBS += 1
            winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), sorted(match), sorted(draws))
        elif len(draws) == 5:
            THREE_NUMBS += 1
            winnings_print((COUNTER/365), len(draws), sorted(QUIT_PICK_FIVE), sorted(match), sorted(draws))
        COUNTER += 1
    # return COUNTER, THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS, SIX_NUMBS

def winnings_print(*args):
    print("\nIt took {:.2f} years to match $$$$$$ {} numbers \n{} <- Your numbers \
    \n{} <- Computer numbers \n{} Matched \n".format(*args))

def print_results(gamesChosen):
    if 'Northstar' in gamesChosen:
        if FOUR_NUMBS == 0 and FIVE_NUMBS == 0:
            print("Sorry!! No winnings! with 4 numbers or more.")

        print("\nOnly the winnings with 4 or more numbers were shown. \nNorthstar!"\
            "\n{} times with 3 numbers.\n{} times with 4 numbers.\n{} times with five"\
             .format(THREE_NUMBS, FOUR_NUMBS, FIVE_NUMBS))
    elif 'Powerball' in gamesChosen:  # TODO:
        pass

def results_powerball(numbOfQuickPicks):
    # Powerball only plays twice in a week, so number of draws is 2.
    powerball4, powerball5, powerball6 = 0, 0, 0
    count = 1
    while count <= numbOfQuickPicks:
        quick_pick_five = set(random.sample(range(1, POWERBALL), 5))
        quick_pick_one = set(random.sample(range(1, POWERPLAY), 1))

        # Draw twice for each week.
        thisCount = 0
        while thisCount < 2:
            draw_five = set(random.sample(range(1, POWERBALL), 5))
            draw_one = set(random.sample(range(1, POWERPLAY), 1))
            draw_five &= quick_pick_five # Find the matches in the fisrt five.
            draw_one &= quick_pick_one   # See if the one matches.
            if len(draw_one) > 0:
                if (len(draw_five) + len(draw_one)) > 2:
                    print("\nWeek number {}:\n{}{}\n{}{}".format(count, sorted(quick_pick_five),\
                                                        draw_one, sorted(draw_five), draw_one))
                    print("Inside the len(draw_one)>0")
            elif len(draw_five) > 2:
                print("\nWeek number {}:\n{}{}\n{}".format(count, sorted(quick_pick_five), sorted(draw_five)))

            thisCount += 1 # Inner loop
        count += 1 # Outer loop
    print()
