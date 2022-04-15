##!/usr/bin/python3

# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

"""
This file contains the dice class as well as
a method to create all dices required for a
game of yahtzee
"""

from random import randint

#TODO Refactor "dice" to "Dice"

class dice:
    '''This class represents a single rollable
       dice
    '''
    def __init__(self):
        self.value = self.roll()
        self.selected = False

    def roll(self):
        '''This function rolls the dice and
           changes its face to a random number
           between 1 and 6

           :returns: None
        '''
        self.value = randint(1, 6)
        return self.value


def get_dices():
    '''This method creates 5 dices.
       This is the amount of dices required for a game of
       yahtzee
    '''
    return [dice() for i in range(5)]
