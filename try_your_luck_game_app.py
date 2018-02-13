import compute_data

GAMES_OPTIONS = ["Powerball", "MegaMillions", "Northstar", "GopherFive",\
"LottoAmerica", "LuckyForLife", "Select All"]

GAMES_CHOSEN = [] # Every time the user selects one, it gets added to this list.

def remove_add_display_game_chosen(numbOfGameChosen):
    for index, val in enumerate(GAMES_OPTIONS):
        if index + 1 == numbOfGameChosen:
            GAMES_CHOSEN.append(val)
            GAMES_OPTIONS.remove(val)

def display_games(games):
    for i, v in enumerate(games):
        print(i + 1, v)

def validate_integer():
    while True: # Validate the user input
        try:
            usr_int = int(input())
            return usr_int
        except:
            print("Enter a number:")

def display_options():

    display_games(GAMES_OPTIONS)
    while True:
        # Display options and loop to get user's chosen ones.
        print("^  Select one option. Type the number (You can add more after one selection)"\
            "\nIf you want to select the rest or all of the other games at the same time"\
            "\nType the number for Select All:")
        game_chosen_numb = validate_integer() # func to get int input only.
        # Any number that is less or greater than the length of GAMES_OPTIONS.
        if game_chosen_numb > len(GAMES_OPTIONS) or game_chosen_numb < 1:
            print("Oops! Number not in list.")
            continue
        # If the selection is the last option, which is select all.
        if game_chosen_numb == len(GAMES_OPTIONS):
            global GAMES_CHOSEN
            [GAMES_CHOSEN.append(game) for game in GAMES_OPTIONS[:-1]]
            break
        # If the above condition are false then.
        else:
            remove_add_display_game_chosen(game_chosen_numb)
            print("\tYour selection so far:")
            display_games(GAMES_CHOSEN)
            print("\tHere are the other options.")
            display_games(GAMES_OPTIONS)
            yes_no = input("\tType:'y/Yes' to add more, else, press 'ENTER' to continue:\n")
            if yes_no.lower() != 'y' or yes_no.lower() != 'yes': continue

def main():
    # Display the games and have the user selec one, etc.
    display_options()

    # Shows the user the games chosen to play.
    print('\n**You selected:')
    display_games(GAMES_CHOSEN)

    # TODO: The option to for the quick pick numbers is the same for all the games.
    # I'd like to change it to where the user cand do it for each game.
    print("\nHow many times do you want to do quick_picks in a year/s? \n e.g."\
        "\n0 = Same numbers all time, \n1 = everyday, \n7 = everyday seven days(weekly),"\
        "\n30 = every month: 'You get the idea :)'")
    numb_of_qpick = validate_integer()

    print("\nEnter the number of years(whole number only) you'd like to try:")
    # Get number of years.
    numb_of_years = validate_integer()

    numb_of_days = numb_of_years * 365 # Need days to compute results.
    print("# " * 40)
    print("Number or years {} \nYour quick pick is 1 every {} day/s".format(numb_of_years, numb_of_qpick))

    # Compute data.
    if "Northstar" in GAMES_CHOSEN:
        compute_data.comp_draws("Northstar", numb_of_qpick, numb_of_days, compute_data.NORTHSTAR)
    if "GopherFive" in GAMES_CHOSEN:
        compute_data.comp_draws("GopherFive", numb_of_qpick, numb_of_days, compute_data.GOPHER5)
    if "Powerball" in GAMES_CHOSEN:
        compute_data.comp_draws("Powerball", numb_of_qpick, numb_of_days, compute_data.POWERBALL, compute_data.POWERPLAY)
    if "MegaMillions" in GAMES_CHOSEN:
        compute_data.comp_draws("MegaMillions", numb_of_qpick, numb_of_days, compute_data.MEGAMILLIONS, compute_data.MEGABALL)
    if "LottoAmerica" in GAMES_CHOSEN:
        compute_data.comp_draws("LottoAmerica", numb_of_qpick, numb_of_days, compute_data.LOTTOAMERICA, compute_data.LOTAMEPOWERPLAY)
    if "LuckyForLife" in GAMES_CHOSEN:
        compute_data.comp_draws("LuckyForLife", numb_of_qpick, numb_of_days, compute_data.LUCKYFORLIFE, compute_data.LUCKYBALL)

if __name__ == "__main__":
    main()
