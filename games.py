import compute_data

game_names = ["Power Ball", "Mega Millions", "North Star", "Gopher Five",\
                        "Lotto America", "Lucky For Life"]
games_selected = [] # Every time the user selects one, it gets added to this list.

def remove_add_display_game_chosen(numbOfGameChosen):
    for index, val in enumerate(game_names):
        if index + 1 == numbOfGameChosen:
            games_selected.append(val)
            game_names.remove(val)

def display_games(games):
    print("=" * 17)
    for i, v in enumerate(games):
        print(i + 1, v)
    print("=" * 17)

def validate_integer():
    while True: # Validate the user input
        try:
            usr_int = int(input())
            return usr_int
        except:
            print("Enter a number:")

def display_options():
    """ Display the instructions at the beginning of the game."""

    display_games(game_names)

    while True:

        # Display options and loop to get user's chosen ones.
        print("{number} = Select all. "\
            "\n^  Select one option."\
            "\nEnter a number:".format(number=len(game_names) + 1))

        game_chosen_numb = validate_integer() # func to get int input only.

        # Any number that is less than one or greater than the length of game_names + 1.
        if game_chosen_numb > len(game_names) + 1 or game_chosen_numb < 1:
            print("-" * 50, "\nOops! Number {} not in list.".format(game_chosen_numb))
            continue
        # If the selection is the last option, which is select all.
        if game_chosen_numb == len(game_names) + 1:
            global games_selected
            [games_selected.append(game) for game in game_names[:-1]]
            break
        # If the above condition are false then.
        else:
            remove_add_display_game_chosen(game_chosen_numb)
            print("-" * 50, "\n\tYour selection so far:")
            display_games(games_selected)
            yes_no = input("Type: 'y/Yes' to add more, else, press 'ENTER' to continue:\n")
            if yes_no.lower() != 'y' and yes_no.lower() != 'yes': break
