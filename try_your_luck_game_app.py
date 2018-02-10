GAMES_OPTIONS = ["Powerball", "Megamillions", "Northstar", "Gopher5",\
"LottoAmerica", "Win_for_life"]

GAMES_CHOSEN = [] # Every time the user selects one, it gets added to this list.

def remove_add_display_game_chosen(numbOfGameChosen):
    if numbOfGameChosen > len(GAMES_OPTIONS) or numbOfGameChosen < 1:
        print("Oops! Number not in list.")
        return
    for index, val in enumerate(GAMES_OPTIONS):
        if index + 1 == numbOfGameChosen:
            GAMES_CHOSEN.append(val)
            GAMES_OPTIONS.remove(val)

def display_games(games):
    for i, v in enumerate(games):
        print(i + 1, v)

def validate_input():
    while True: # Validate the user input
        try:
            usr_int = int(input())
            return usr_int
        except:
            print("Enter a number:")

def display_options(msg):
    while True:
        display_games(GAMES_OPTIONS)
        print(msg)
        game_chosen_numb = validate_input() # func to get int input only.
        remove_add_display_game_chosen(game_chosen_numb)
        print("\nYour selection so far:")
        display_games(GAMES_CHOSEN)
        yes_no = input("Do you want to add another game? y/n:\n")
        if yes_no.lower() != 'y': break

def main():
    # This is to let the user know what needs to entered.
    msg_numb_years = "Enter the number of years(whole number only) you'd like to try:"
    msg_select_one = "^^Select one option. Enter the number:"

    display_options(msg_select_one)

    display_games(GAMES_CHOSEN)
    # numb_of_years = validate_input(msg_numb_years) # get an int.

if __name__ == "__main__":
    main()
