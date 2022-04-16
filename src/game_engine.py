#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''This module contains the games main loop
   and general controll unit
'''

from src.tui_engine import TuiEngine
from src.dices import Dice
from src.player import new_players
from src.term_info import terminal 

class GameEngine():
    '''The main backend of the game
    '''
    def __init__(self):
        self.tui = TuiEngine()
        self.terminal = terminal() 
        self.actions = 3
        self.players = new_players()
        self.dices = get_dices()

    def handle_input(self):
        key = self.terminal.getch()

        if key.isnumeric() and int(key) in range(1, 6):
            dices[int(key)-1].switch()

        elif key == 'q':
            self.terminal.clear()
            sys.exit(0)

        elif ord(key) == 13: # 13 <=> 'Enter':
            # player has to select the rule he wants to use
            # calc score
            # next players turn

        elif ord(char) == 32: # 32 <=> 'Space'
            # roll dice 

        # log if necessary

    def run(self):
        '''Contains the main loop of the game
        '''
        while True:
            # draw game
            handle_input()
