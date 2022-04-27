#!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

"""
Class for handeling one player in the game
"""

from random import getrandbits

from src.dices import get_dices
from src.rules import CATEGORIES, CATEGORY_FUNCTIONS, OPTIONS

class Player:
    '''This class represents a single player.
       Can calculate the players score and stores
       a username.
    '''
    def __init__(self, name, active = False):
        self.name   = name
        self.active = active
        self.table  = []

        self.dices      = get_dices()
        self.scores     = [ 0 ]     * len(CATEGORIES)
        self.used_rules = [ False ] * len(CATEGORY_FUNCTIONS)

    def load_from_dict(self, data: []):
        '''This method loads a players data from a dictionary

           :param data: The dict the data is loaded from
           :returns: None
        '''
        self.name = data["name"]
        for i, dice_value in enumerate(data["dices"]):
            self.dices[i].value = dice_value

        for i, flag in enumerate(data["flags"]):
            self.used_rules[i] = flag

        for i, score in enumerate(data["scores"]):
            self.scores[i] = score

    def get_all_dice_faces(self) -> []:
        '''Get all dice values

           :returns: All dice faces as integers
        '''
        return [ dice.value for dice in self.dices ]

    def get_selected_dice_faces(self) -> []:
        '''Get all faces of selected dices.
           This is used for displayment purposes.

           :returns: All selected dice faces
        '''
        return [ dice.value for dice in self.dices if dice.selected ]

    def get_options(self) -> []:
        '''
        Returns list with values for each rule for the currently selected dice faces
        '''
        options = []
        for index, function in enumerate(CATEGORY_FUNCTIONS):
            is_rule, value = function([ dice.value for dice in self.dices ])
            if not self.used_rules[index]:
                options.append((OPTIONS[index], value))

            if self.used_rules[index] and function.__name__ == "yahtzee" and is_rule:
                options.append(OPTIONS[index], value+self.dices[0].value * len(self.dices))

        return options

    def calculate_scores(self):
        '''Calculate the current score of the player

           :returns: None
        '''
        self.scores[7]  = sum(self.scores[1:7])
        self.scores[8]  = 35 if self.scores[7] > 62 else 0
        self.scores[16] = sum(self.scores[7:16])

    def reset_dice(self):
        '''Deselect and reroll all dice

           :returns: None
        '''
        for i, _ in enumerate(self.dices):
            self.dices[i].roll()
            self.dices[i].selected = False

    def get_score(self):
        '''Get the total score of a player

           :returns: The total amount of points the player has collected
        '''
        return sum(score for score in self.scores)


def new_players(name_one = "PLAYER 1", name_two = "PLAYER 2"):
    '''Generate two new players with a selectable username.
       Randomly select who goes first.

       :param name_one: Name of player one
       :param name_two: Name of player two
       :returns: None
    '''
    return (Player(name_one, True), Player(name_two))\
                if bool(getrandbits(1))\
                else (Player(name_two, True), Player(name_one))
