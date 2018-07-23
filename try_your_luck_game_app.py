import compute_data

GAMES_OPTIONS = ["Powerball", "MegaMillions", "Northstar", "GopherFive",\
"LottoAmerica", "LuckyForLife"]

select_all = len(GAMES_OPTIONS)

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

    while True:
        display_games(GAMES_OPTIONS)
        # Display options and loop to get user's chosen ones.
        print("^  Select one option. Type the number (You can add more after one selection)"\
            "\nIf you want to select the rest or all of the other games at the same time"\
            "\nType the {number} for Select All:".format(number=len(GAMES_OPTIONS)))
        game_chosen_numb = validate_integer() # func to get int input only.
        # Any number that is less or greater than the length of GAMES_OPTIONS.
        if game_chosen_numb > len(GAMES_OPTIONS) or game_chosen_numb < 1:
            print("-" * 50, "\nOops! Number {} not in list.".format(game_chosen_numb))
            continue
        # If the selection is the last option, which is select all.
        if game_chosen_numb == len(GAMES_OPTIONS):
            global GAMES_CHOSEN
            [GAMES_CHOSEN.append(game) for game in GAMES_OPTIONS[:-1]]
            break
        # If the above condition are false then.
        else:
            remove_add_display_game_chosen(game_chosen_numb)
            print("-" * 50, "\n\tYour selection so far:")
            display_games(GAMES_CHOSEN)
            yes_no = input("Type: 'y/Yes' to add more, else, press 'ENTER' to continue:\n")
            if yes_no.lower() != 'y' and yes_no.lower() != 'yes': break

def main():
    # Display the games and have the user selec one, etc.
    display_options()

    # Shows the user the games chosen to play.
    print('\n**You selected:')
    display_games(GAMES_CHOSEN)

    while True:
        print("Enter the number of years(whole number only) that you'd like to try:")
        # Get number of years.
        numb_of_years = validate_integer()
        if numb_of_years < 1 or numb_of_years > 30:
            print("Lets keep the number of years between 1 and 30")
        else: break

    numb_of_days = numb_of_years * 365 # Need days to compute results.

    while True:
        print("\nHow many times do you want to do quick_picks in the {} year/s you entered?"\
        "\n1 = Same quick pick all time?, \n7 = weekly?, \n14 = every two weeks?,"\
        "\n21 = every three weeks?, or \n28 = every month?:".format(numb_of_years))
        numb_of_qpick = validate_integer()
        if numb_of_qpick != 1 and numb_of_qpick != 7 and numb_of_qpick != 14\
                and numb_of_qpick != 21 and numb_of_qpick != 28:
            print("\n Oops! Enter one number in options only. try again!")
        else: break

    print("# " * 40)
    print("Number or years {} \nYour quick pick is 1 every {} day/s \n----------------------\n".format(numb_of_years, numb_of_qpick))

    # Compute data.
    if "Northstar" in GAMES_CHOSEN:
        compute_data.comp_draws("Northstar", numb_of_qpick, numb_of_days, compute_data.NORTHSTAR, 7)
    if "GopherFive" in GAMES_CHOSEN:
        compute_data.comp_draws("GopherFive", numb_of_qpick, numb_of_days, compute_data.GOPHER5, 3)
    if "Powerball" in GAMES_CHOSEN:
        compute_data.comp_draws("Powerball", numb_of_qpick, numb_of_days, compute_data.POWERBALL, 2, compute_data.POWERPLAY)
    if "MegaMillions" in GAMES_CHOSEN:
        compute_data.comp_draws("MegaMillions", numb_of_qpick, numb_of_days, compute_data.MEGAMILLIONS, 2, compute_data.MEGABALL)
    if "LottoAmerica" in GAMES_CHOSEN:
        compute_data.comp_draws("LottoAmerica", numb_of_qpick, numb_of_days, compute_data.LOTTOAMERICA, 2, compute_data.LOTAMEPOWERPLAY)
    if "LuckyForLife" in GAMES_CHOSEN:
        compute_data.comp_draws("LuckyForLife", numb_of_qpick, numb_of_days, compute_data.LUCKYFORLIFE, 2, compute_data.LUCKYBALL)

    compute_data.totalFourOrPlus()

if __name__ == "__main__":
    main()
