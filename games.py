import compute_data

game_names = ["Power Ball", "Mega Millions", "North Star", "Gopher Five",\
                        "Lotto America", "Lucky For Life"]
games_selected = [] # Every time the user selects one, it gets added to this list.

def game_chosen_add_and_remove(numb_selected):
    for index, val in enumerate(game_names):
        if index + 1 == numb_selected:
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
    """
    Display the instructions at the beginning of the game.
    The user can select one game at a time or select all.
    """

    while True:
        # Display list of games still not selected, list will shrink as user selects.
        display_games(game_names)

        print("{number} = Select all. "\
            "\n^  Select one option or press 'Control ^ z' to Exit"\
            "\nEnter a number:".format(number=len(game_names) + 1))

        # This will make sure that the number entered is an integer only.
        numb_selected = validate_integer()

        # Any number that is less than one or greater than the length of game_names + 1.
        # +1 is because we want the user be able to select all options.
        if numb_selected > len(game_names) + 1 or numb_selected < 1:
            print("-" * 50, "\n---->Oops! Number {} not in list.".format(numb_selected))
            continue
        elif numb_selected == len(game_names) + 1:
            global games_selected
            [games_selected.append(game) for game in game_names]
            print("*You have selected...")
            return display_games(games_selected)
        else:
            game_chosen_add_and_remove(numb_selected)
            print("-" * 50, "\n\tYour selection so far:")
            display_games(games_selected)
            yes_no = input("Type: 'y/Yes' to add more, else, press 'ENTER' to continue:\n")
            if yes_no.lower() != 'y' and yes_no.lower() != 'yes': break
