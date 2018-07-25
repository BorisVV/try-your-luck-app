from abc import ABCMeta, abstractmethod
class Game(object):
    '''
    Each game has a name, numb_of_qpick, number of years.
    '''
    __metaclass__ = ABCMeta

    def __init__(self, name, numb_of_qpick, numb_of_years):
        self.name = name
        self.numb_of_qpick = numb_of_qpick
        self.numb_of_days = numb_of_years * 365 # Need to convert to days.


#     "Power Ball": 70,
#     "Power Play": 27,
#     "Gopher Five": 48,
#     "North Star": 32,
#     "Lotto America": 53,
#     "Star Ball": 11,
#     "Mega Millions": 71,
#     "Mega Ball": 26,
#     "Lucky For Life": 49,
#     "Lucky Ball": 19,

'''For each of the games we'll use the quick pick method where the computer selects the number. '''

class NorthStar(Game):
    '''
    North Star has 31 numbers and the computer will select five.
    '''
    north_star = 31 # When using the range method, add 1.
    x_in_a_week = 7 # Number of times it plays each week.

    def __init__()
