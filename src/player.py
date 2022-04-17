#!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

"""
Class for handeling one player in the game
"""

from random import getrandbits

from src.dices import get_dices
from src.rules import CATEGORIES,\
                  CATEGORY_FUNCTIONS


class Player:
    '''This class represents a single player.
       Can calculate the players score and stores
       a username.
    '''
    def __init__(self, name, active = False):
        self.name = name
        self.active = active
        self.table = []

        self.dices = get_dices()
        self.scores = [ 0 for i in range(len(CATEGORIES)) ]

    def get_options(self) -> []:
        '''
        Returns list with values for each rule for the currently selected dice faces
        '''
        selected_dice_faces = [ dice.value for dice in self.dices if dice.selected ]
        options = []
        for index, function in enumerate(CATEGORY_FUNCTIONS):
            res, value = function(selected_dice_faces)
            if res:
                options.append((CATEGORIES[index+1], value))
        return options

    def calculate_scores(self):
        '''Calculate the current score of the player

           :returns: None
        '''
        self.scores[7] = sum(self.scores[1:7])
        self.scores[8] = 35 if self.scores[7] > 62 else 0
        self.scores[16] = sum(self.scores[7:16])

    def reset_dice(self):
        '''Deselect all players dice

           :returns: None
        '''
        for i, _ in enumerate(self.dices):
            self.dices[i].selected = False


def new_players(name_one = "PLAYER 1", name_two = "PLAYER 2"):
    '''Generate two new players with a selectable username.
    name_one, name_two   Randomly select who goes first.

       :param name_one: Name of player one
       :param name_two: Name of player two
       :returns: None
    '''
    if bool(getrandbits(1)):
        return Player(name_one, True), Player(name_two)
    return Player(name_two, True), Player(name_one)
