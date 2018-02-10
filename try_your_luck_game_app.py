import compute_data

GAMES_OPTIONS = ["Powerball", "MegaMillions", "Northstar", "GopherFive",\
"LottoAmerica", "WinForlife"]

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
    numb_of_years = 0
    while True:
        display_games(GAMES_OPTIONS)
        print(msg)
        game_chosen_numb = validate_input() # func to get int input only.
        remove_add_display_game_chosen(game_chosen_numb)
        print("\nYour selection so far:")
        display_games(GAMES_CHOSEN)
        yes_no = input("\nDo you want to add another game? \ntype:'y' to continue:"\
                        " or press 'Enter' to Exit:\n")
        if yes_no.lower() != 'y': break

def main():
    # This is to let the user know what needs to entered.
    msg_select_one = "\n^ Select one option. Enter the number:"

    # Display the games and have the user selec one, etc.
    display_options(msg_select_one)

    # Shows the user the games chosen to play.
    print('You selected:')
    display_games(GAMES_CHOSEN)

    print("\nEnter the number of years(whole number only) you'd like to try:")
    # Get number of years.
    numb_of_years = validate_input()

    # Let the luck begin..
    compute_data.compute_games_chosen(numb_of_years, GAMES_CHOSEN)

if __name__ == "__main__":
    main()
