from game_class import Game
import random

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

    def calculate(self):
        self.numbers1 = 31 + 1 #When using range for loops the last number is not counted.
        self.counter = 1
        insideLoopCounter = 0
        if self.numb_of_qpick == 1:
            self.numb_of_weeks *= 7
            while self.counter <= self.numb_of_weeks:
                Game.userQPickFive(self)
                # Change the number in the perimeter between 1 and 5.
                Game.computerDrawingFives(self, 3)
                self.counter += 1
        # User decides to buy once every week and the ticket is good for 7 drawings.
        elif self.numb_of_qpick == 2:
            self.numb_of_qpick = 7
            while self.counter <= self.numb_of_weeks:
                insideLoopCounter = 1
                Game.userQPickFive(self)
                # Every week, we need to update the quick pick drawing for the user.
                while insideLoopCounter <= self.numb_of_qpick: # number of times North Star drawings.
                    Game.computerDrawingFives(self, 3)
                    insideLoopCounter += 1
                self.counter += 1
        # User selected one quick pick that is good for two weeks, or fourteen drawings.
        else:
            self.numb_of_qpick = 14
            while self.counter <= self.numb_of_weeks:
                insideLoopCounter = 1
                Game.userQPickFive(self)
                while insideLoopCounter <= self.numb_of_qpick:
                    Game.computerDrawingFives(self, 3)
                    insideLoopCounter += 1
                self.counter += 2

    def get_name(self):
        return self.name

    def get_numb_qpicks(self):
        print(self.numb_of_qpick)



class GopherFive(Game):
    ''' This game plays 3 times a week. e.g. if user enters 2 for the numb of qpicks,
        wich is 1 week, that means that the ticket is valid to play for 3 drawings. The same numbers will be matched against 3 drawing and then, the user's numbers will
        be drawn again, repeating the sequence until the number of weeks are done..
    '''
    def calculate(self):
        self.numbers1 = 48 + 1
        self.counter = 1
        insideLoopCounter = 0 #This is for every ticket, loop three times.
        # User buys a ticket 3 times a week, every week.
        if self.numb_of_qpick == 1: #One quick pick for every drawing.
            self.numb_of_weeks *= 3 #where 3 is the number that gopher five plays
                # everyweek times the total number of week in a the years entered.
            while self.counter <= self.numb_of_weeks:
                Game.userQPickFive(self)
                # Change the number in the perimeter between 1 and 5.
                Game.computerDrawingFives(self, 2)
                self.counter += 1

        # User buys a ticket that is good for 3 drawing (full week).
        elif self.numb_of_qpick == 2: #User buys quick pick once everyweek.
            self.numb_of_qpick = 3
            while self.counter <= self.numb_of_weeks:
                insideLoopCounter = 1
                Game.userQPickFive(self)
                while insideLoopCounter <= self.numb_of_qpick:
                    Game.computerDrawingFives(self, 2)
                    insideLoopCounter += 1
                self.counter += 1
        else:
            self.numb_of_qpick = 6
            while self.counter <= self.numb_of_weeks:
                insideLoopCounter = 1
                Game.userQPickFive(self)
                while insideLoopCounter <= self.numb_of_qpick:
                    Game.computerDrawingFives(self, 2)
                    insideLoopCounter += 2
                self.counter += 2

    def get_name(self):
        return self.name

    def get_numb_qpicks(self):
        return self.numb_of_qpick
