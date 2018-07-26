from abc import ABCMeta, abstractmethod
import random

class Game(object):
    '''
    Each game has a name, numb_of_qpick, number of years.
    '''
    __metaclass__ = ABCMeta

    numbers1 = 0 #games numbers that the user has to pick from.
    numbers2 = 0 #e.g. MegaMillions has a power play, this is for that.
    userFiveNumbsSet = set() #This creates a list of five numbers, randonly selected.
    userOneNumbSet = set() #This will create a list with one number, set is isiers to match.
    computer_draws_five = set()
    computer_draws_one = set()

    listCoumputerDrawsFive = []
    listCoumputerDrawsOne = []

    def __init__(self, numb_of_qpick, numb_of_years):
        self.numb_of_qpick = numb_of_qpick
        self.numb_of_weeks = (numb_of_years * 365) // 7 # Need to convert to numb_of_weeks.

    @abstractmethod
    def get_name(self):
        ''' Return the name of the game being called.'''
        pass

    @abstractmethod
    def calculate(self):
        ''' This will get the result for the game. '''
        pass

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

#For each of the games we'll use the quick pick where the computer
#selects the number. '''

class NorthStar(Game):
    '''
    North Star has 31 numbers and the computer will select five for the quick pick and the drawings.
    '''

    def get_name(self):
        return 'North Star'

    def calculate(self):
        numbers1 = 31 + 1 #When using range for loops the last number is not counted.
        if self.numb_of_qpick == 1:
            self.numb_of_qpick = self.numb_of_weeks
            for i in range(1, self.numb_of_qpick):
                #get the numbers for the user/player.
                userFiveNumbsSet = set(random.sample(range(1, numbers1), 5))
                #get computer numbers.
                computer_draws_five = set(random.sample(range(1, numbers1), 5))
                #the next line needs to convert computer_draws_five to list or else,
                #it will affect the output of the displayComputerDrawsFive.
                displayComputerDrawsFive = list(computer_draws_five)
                computer_draws_five &= userFiveNumbsSet #only keep matching numbers.
                if len(computer_draws_five) > 2:
                    print("\n------\n your numbers ", sorted(userFiveNumbsSet))
                    print("Winnings with 3 or more #'s ", sorted(computer_draws_five))
                    print("computer numbers ", sorted(displayComputerDrawsFive))


class GopherFive(Game):

    def get_name(self):
        return 'Gopher Five'

    def calculate(self):
        numbers1 = 48 + 1

        if self.numb_of_qpick == 1:
            while self.numb_of_weeks > 0:
                #This gamea is played 3 times a week. This is the reason for 3.
                self.numb_of_qpick = 3 #Gopher five plays 3 times a week
                while self.numb_of_qpick > 0:
                    #get the numbers for the user/player.
                    userFiveNumbsSet = set(random.sample(range(1, numbers1), 5))
                    computer_draws_five = set(random.sample(range(1, numbers1), 5))
                    #the next line needs to convert computer_draws_five to list or else,
                    #it will affect the output of the displayComputerDrawsFive.
                    displayComputerDrawsFive = list(computer_draws_five)
                    computer_draws_five &= userFiveNumbsSet #only keep matching numbers.
                    if len(computer_draws_five) > 2:
                        print('\nGopherFive')
                        print("\nWon on {} ".format(self.numb_of_weeks))
                        print("------\n your numbers ", sorted(userFiveNumbsSet))
                        print("Winning numbers ", sorted(computer_draws_five))
                        print("computer numbers ", sorted(displayComputerDrawsFive))
                    self.numb_of_qpick -= 1
                self.numb_of_weeks -= 1
