##!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

'''
This file contains the dice class as well as
a method to create all dices required for a
game of yahtzee
'''

from random import randint

class Dice:
    '''This class represents a single rollable
       dice
    '''
    def __init__(self):
        self.roll()
        self.selected = False

    def roll(self):
        '''This function rolls the dice and
           changes its face to a random number
           between 1 and 6

           :returns: None
        '''
        self.value = randint(1, 6)
        return self.value

    def switch(self):
        '''Toggle selected status of the dice

           :returns: None
        '''
        self.selected = not self.selected


def get_dices():
    '''This method creates 5 dices.
       This is the amount of dices required for a game of
       yahtzee
    '''
    return [ Dice() for i in range(5) ]

def reset_dices(dices):
    '''Renew the status of all dices to not selected
       and assign a new value to each one.
        This is the equivalent to one turn in yahtzee.

        :param dices: A list of all dices that are supposed to be reset
        :returns: None
    '''
    for current_dice in dices:
        current_dice.selected = False
        current_dice.roll()
