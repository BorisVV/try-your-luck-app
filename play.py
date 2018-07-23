import games as g

def main():
    '''Display instructions to select games then enter years followed by how many times'''

    g.display_options()

    # User needs to enter a whole number, between the range set.
    while True:
        print("Press 'Control ^ z' to Exit or"\
              "\nEnter the number of years(whole number only) that you'd like to try:")
        # Get number of years.
        numb_of_years = g.validate_integer()
        if numb_of_years < 1 or numb_of_years > 30:
            print("---Error-Lets keep the number of years between 1 and 30")
            continue
        else: break

    # Total number of days in the number of years enteed by user.
    numb_of_days = numb_of_years * 365 # Need days to compute results.

    while True:
        # Games are played different, like once a day or twice a week, etc.
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
    if "Northstar" in games_selected:
        compute_data.comp_draws("Northstar", numb_of_qpick, numb_of_days, compute_data.NORTHSTAR, 7)
    if "GopherFive" in games_selected:
        compute_data.comp_draws("GopherFive", numb_of_qpick, numb_of_days, compute_data.GOPHER5, 3)
    if "Powerball" in games_selected:
        compute_data.comp_draws("Powerball", numb_of_qpick, numb_of_days, compute_data.POWERBALL, 2, compute_data.POWERPLAY)
    if "MegaMillions" in games_selected:
        compute_data.comp_draws("MegaMillions", numb_of_qpick, numb_of_days, compute_data.MEGAMILLIONS, 2, compute_data.MEGABALL)
    if "LottoAmerica" in games_selected:
        compute_data.comp_draws("LottoAmerica", numb_of_qpick, numb_of_days, compute_data.LOTTOAMERICA, 2, compute_data.LOTAMEPOWERPLAY)
    if "LuckyForLife" in games_selected:
        compute_data.comp_draws("LuckyForLife", numb_of_qpick, numb_of_days, compute_data.LUCKYFORLIFE, 2, compute_data.LUCKYBALL)

    compute_data.totalFourOrPlus()

if __name__ == "__main__":
    main()
