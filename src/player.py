#!/usr/bin/python3

# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

"""
Class for handeling one player in the game
"""

from dices import get_dices
from random import getrandbits
from rules import CATEGORIES


#for rule in RULES:
#    exec(f"from rules import {rule}")

#RULES_FUNCTION_POINTER = [ eval(item) for item in RULES ]
from rules import CATEGORY_FUNCTIONS

class Player:
    def __init__(self, name, active = False):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

        self.dices = get_dices()
        #for key in CATEGORIES[1:]:
        #    self.scoreboard[key] = None

    def get_options(self, dices):
        """
        Returns list with values for each rule for the currently selected dice faces
        """
        selected_dice_faces = [ dice.value for dice in dices if dice.selected ]
        options = []
        for index, function in enumerate(CATEGORY_FUNCTIONS):
            res, value = function(selected_dice_faces)
            if res:
                options.append((CATEGORIES[index+1], value))

        #for counter, function in enumerate(RULES_FUNCTION_POINTER):
        #    return [ {} for opt in selected if  ]








def new_players(name_1, name_2):
    if getrandbits(1):
        return Player(name_1, True), Player(name_2)
    else:
        return Player(name_2, True), Player(name_1)


if __name__ == "__main__":
    p = Player("Peter", True)
    print(p.active)

