#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''This module contains the games main loop
   and general controll unit
'''

from src.tui_engine import TuiEngine
from src.dices import Dice
from src.player import new_players

class GameEngine():
    '''The main backend of the game
    '''
    def __init__(self):
        self.tui = TuiEngine()
        self.actions = 3
        self.players = new_players()
        self.dices = get_dices()

    def run(self):
        '''Contains the main loop of the game
        '''
        while True:
            pass
