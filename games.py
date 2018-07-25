import compute_data
import time

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
            print("OOps!! Enter a valid number:")

def display_options():
    """
    Display the instructions at the beginning of the game.
    The user can select one game at a time or select all.
    """

    while True:
        if len(game_names) == 0:
            break
        # Display list of games still not selected, list will shrink as user selects.
        display_games(game_names)

        print("{number} = Select all. \n^  Select one option or press 'Control ^ z' to Exit:".format(number=len(game_names) + 1))

        # This will make sure that the number entered is an integer only.
        numb_selected = validate_integer()

        # Any number that is less than one or greater than the length of game_names + 1.
        # +1 is because we want the user be able to select all options.
        if numb_selected > len(game_names) + 1 or numb_selected < 1:
            print("-" * 50, "\n---->Oops! Number {} not in list.".format(numb_selected))
            time.sleep(3)
            continue
        elif numb_selected == len(game_names) + 1:
            global games_selected
            [games_selected.append(game) for game in game_names]
            print("*You have selected...")
            return display_games(games_selected)
        else:
            game_chosen_add_and_remove(numb_selected)
            print("-" * 50, "\n\n\tYour selection so far:")
            display_games(games_selected)
            yes_no = input("\nAdd more? \n'y' / 'Yes' or (press 'ENTER' or any other key to Exit and continue. \nPress 'Control ^ z' to Exit:")
            if yes_no.lower() != 'y' and yes_no.lower() != 'yes': break

def getNumberOfYears():
    # User needs to enter a whole number, between the range set.
    while True:
        print("\n>>>Next step. \nNumber of years(whole numbers only) that you'd like to try \nPress 'Control ^ z' to Exit:")
        # Get number of years.
        numb_of_years = validate_integer()
        if numb_of_years < 1 or numb_of_years > 30:
            print("---Error!---Lets keep the number of years between 1 and 30")
            time.sleep(3)
            continue
        else:
            return numb_of_years

def getNumbOfQuickPicks(numb_of_years):
    while True:
        # Games are played different, like once a day or twice a week, etc.
        print("\n>>>Next step.\n(Some games play daily, others 2 e.g. week=(2*week), etc.) \nHow frequently do you want to do quick_picks in the number of {} year/s that you entered? \n1 = Once?, \n2 = weekly? , \n3 = every two weeks? \n4 = every three weeks? or \n5 = every month? \nPress 'Control ^ z' to Exit:".format(numb_of_years))
        numb_of_qpick = validate_integer()
        if numb_of_qpick != 1 and numb_of_qpick != 2 and numb_of_qpick != 3\
                and numb_of_qpick != 4 and numb_of_qpick != 5:
            print("\n Oops! Enter one number from the options only. try again!")
            time.sleep(3)
            continue
        return numb_of_qpick
