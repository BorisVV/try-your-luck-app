import games as _g
import compute_data as _c_d
from games_classes import NorthStar, GopherFive

def main():
    '''Display instructions to select games then enter years followed by how many times'''

    _g.display_options()

    # This will return the number of years the user wants to play the numbers.
    numb_of_years = _g.getNumberOfYears()

    # Get the quickpicks selection, it can be weekly, every two weeks, etc..
    numb_of_qpick = _g.getNumbOfQuickPicks(numb_of_years)

    print("\n" + "# " * 40)
    print("Number or years entered {} \n----------------------\n".format(numb_of_years))


    ns = NorthStar("North Star", numb_of_qpick, numb_of_years)
    gf = GopherFive("Gopher Five", numb_of_qpick, numb_of_years)

    if "North Star" in _g.games_selected:
        ns.calculate()
    if "Gopher Five" in _g.games_selected:
        gf.calculate()




    # Compute data.
    # if "North Star" in _g.games_selected:
    #     _c_d.comp_draws("Northstar", numb_of_qpick, numb_of_days, _c_d.NORTHSTAR, 7)
    # if "Gopher Five" in _g.games_selected:
    #     _c_d.comp_draws("GopherFive", numb_of_qpick, numb_of_days, _c_d.GOPHER5, 3)
    # if "Power Ball" in _g.games_selected:
    #     _c_d.comp_draws("Powerball", numb_of_qpick, numb_of_days, _c_d.POWERBALL, 2, _c_d.POWERPLAY)
    # if "Mega Millions" in _g.games_selected:
    #     _c_d.comp_draws("MegaMillions", numb_of_qpick, numb_of_days, _c_d.MEGAMILLIONS, 2, _c_d.MEGABALL)
    # if "Lotto America" in _g.games_selected:
    #     _c_d.comp_draws("LottoAmerica", numb_of_qpick, numb_of_days, _c_d.LOTTOAMERICA, 2, _c_d.LOTAMEPOWERPLAY)
    # if "Lucky For Life" in _g.games_selected:
    #     _c_d.comp_draws("LuckyForLife", numb_of_qpick, numb_of_days, _c_d.LUCKYFORLIFE, 2, _c_d.LUCKYBALL)
    #
    # _c_d.totalFourOrPlus()

if __name__ == "__main__":
    main()
