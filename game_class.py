from abc import ABCMeta, abstractmethod
import random

class Game(object):
    '''
    Each game has a name, numb_of_qpick, number of years.
    '''
    __metaclass__ = ABCMeta

    def __init__(self, name, numb_of_qpick, numb_of_years):
        self.name = name
        self.numb_of_qpick = numb_of_qpick
        # Need to convert to numb_of_weeks.
        self.numb_of_weeks = (numb_of_years * 365) // 7
         #This creates a list of five numbers, randonly selected.
        self.userFiveNumbsSet = set()
        #This will create a list with one number, set is isiers to match.
        self.userOneNumbSet = set()

        self.computer_draws_five = set()
        self.computer_draws_one = set()

        self.listCoumputerDrawsFive = []
        self.listCoumputerDrawsOne = []

        self.numbers1 = 0 #games numbers that the user has to pick from.
        self.numbers2 = 0 #e.g. MegaMillions has a power play, this is for that.
        self.counter = 0

    @abstractmethod
    def get_name(self):
        ''' Return the name of the game being called.'''
        pass

    @abstractmethod
    def calculate(self):
        ''' This will get the result for the game. '''
        pass

    @abstractmethod
    def userQPickFive(self):
        #get the numbers for the user/player.
        self.userFiveNumbsSet = set(random.sample(range(1, self.numbers1), 5))

    @abstractmethod
    def compDrawingFive(self, numb):
        #draw the computer drawings.
        self.computer_draws_five = set(random.sample(range(1, self.numbers1), 5))
        #the next line needs to convert computer_draws_five to list or else,
        #it will affect the output of the displayComputerDrawsFive.
        self.displayComputerDrawsFive = list(self.computer_draws_five)
        self.computer_draws_five &= self.userFiveNumbsSet #only keep matching numbers.
        if len(self.computer_draws_five) > int(numb):
            print("\n------\n{} \nWon on try number {} \nYour numbers {}\nWinnings with 3 or more #'s {} \nComputer numbers {}".format(self.name, self.counter, sorted(self.userFiveNumbsSet), sorted(self.computer_draws_five), sorted(self.displayComputerDrawsFive)))
