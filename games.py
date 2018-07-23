import compute_data

class Games:
    """docstring for Game."""
    def __init__(self, *arg):
        self.arg = arg

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
