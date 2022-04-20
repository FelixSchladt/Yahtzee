#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''This module contains the games main loop
   and general controll unit
'''

import sys
from src.tui_engine import TuiEngine,\
                           RoundsBox,\
                           draw_dices,\
                           draw_player_tables,\
                           category_table,\
                           log
from src.dices import get_dices
from src.player import new_players
from src.rules import CATEGORIES, CATEGORY_FUNCTIONS
from src.term_info import terminal

class GameEngine():
    '''The main backend of the game
    '''
    def __init__(self):
        self.tui = TuiEngine()
        self.round_box = RoundsBox(self.tui)
        self.terminal = terminal()
        self.turns = 3
        # TODO add better name input -> maybe as varargs?? -> much easier than menu
        self.players = new_players()
        self.dices = get_dices()

    def handle_input(self):
        '''This method is resposible for executing the
           correct methods after a certain key is pressed

           :returns: None
        '''
        key = self.terminal.getch()

        if key.isnumeric() and int(key) in range(1, 6):
            active = self.get_active_player_index()
            self.players[active].dices[int(key)-1].switch()

        elif key == 'q':
            self.terminal.clear()
            sys.exit(0)

        elif ord(key) == 13: # 'Enter'
            self.end_turn()

        elif ord(key) == 32: # 'Space'
            self.roll_dice()

        log(f"Input read: {key}")

    def end_turn(self):
        '''Executes when the player presses Enter.
           Will end a players turn.
           The player has to select a rule he want to use.
        '''
        active = self.get_active_player_index()
        if not self.player_done(active):
            if len(self.players[active].get_options()) > 0:
                self.select_rule()

        for i, _ in enumerate(self.players):
            self.players[i].calculate_scores()
            self.players[i].active = not self.players[i].active
            self.players[i].reset_dice()

        self.turns = 3

    def select_rule(self):
        '''This method lets the player select the rule he wants to
           collect points for at the end of his turn

           :returns:
        '''
        active = self.get_active_player_index()
        options = self.players[active].get_options()
        selection = -1

        self.terminal.clear()
        print(f"{self.players[active].name} chooses an option:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        while True:
            try:
                selection = int(
                            input(f"Input (1-{len(options)}): "))\
                            - 1

                if not selection in range(len(options)):
                    print("Invalid input, try again!")
                    continue
                break

            except Exception:
                print("Invalid input, try again!")
                continue

        # Get indices required to read and write the correct
        # results to the player object
        selected_option = options[selection][0]
        formated_option = selected_option.lower().replace(' ', '_')

        scoreboard_index = [i for i in range(len(CATEGORIES))\
                         if CATEGORIES[i] == selected_option][0]
        function_index = [i for i in range(len(CATEGORY_FUNCTIONS))\
                         if formated_option == CATEGORY_FUNCTIONS[i].__name__][0]

        # Set player score[index] to correct score
        self.players[active].scores[scoreboard_index] = CATEGORY_FUNCTIONS[function_index](
                self.players[active].get_all_dice_faces())[1]

        self.players[active].used_rules[function_index] = True

        if self.game_over():
            exit(0)
            winner = self.players[0].name if self.players[0].get_score() > self.players[1].get_score() else self.player[1].name

            #TODO make this a little more beautiful
            self.terminal.clear()
            print(f"The winner of the game is: {winner}")
            input("Press 'Enter' to exit")
            exit(0)

    def roll_dice(self):
        '''Executes when the user presses space.
           Will roll all deselected dice.
           This action costs one of the three turns each player has.

           :returns: None
        '''
        active = self.get_active_player_index()
        for i, _ in enumerate(self.players[active].dices):
            if not self.players[active].dices[i].selected:
                self.players[active].dices[i].roll()

        self.turns -= 1

        if self.turns == 0:
            self.end_turn()

    def draw_game(self):
        '''Draws the game on the terminal

           :returns: None
        '''
        active = self.get_active_player_index()

        self.tui.frame()
        self.round_box.set_round(self.turns)

        draw_dices(self.tui, self.players[active].dices)
        category_table(self.tui)
        draw_player_tables(self.tui, self.players)
        self.round_box.draw()
        self.tui.text(2, 18, f"Player: {self.players[self.get_active_player_index()].name}"\
                "                ")
        self.tui.text(2, 20, "Selected                  ")
        self.tui.text(2, 20, "Selected: "\
                f"{self.players[active].get_selected_dice_faces()}")
        self.tui.text(2, 22, "Options: "\
                f"{self.players[active].get_options()[:6]}")
        self.tui.flush()

    def get_active_player_index(self) -> int:
        '''This method returns the index of
           the player that is currently playing.

           :returns: The index of the playing player
        '''
        active_index = 0
        for i, _ in enumerate(self.players):
            if self.players[i].active:
                active_index = i
        return active_index

    def game_over(self):
        '''Check if the board is full
           Display winscreen and end game if yes

           :returns: None
        '''
        game_over = True
        for i, _ in enumerate(self.players):
            if not self.player_done(i):
                game_over = False

        return game_over

    def player_done(self, index: int) -> bool:
        '''Checks if a player has filled his board

           :returns: True if the player filled his board
                     else False
        '''
        done = True
        for rule_used in self.players[index].used_rules:
            if not rule_used:
                done = False
                break

        return done

    def run(self):
        '''Contains the main loop of the game
        '''
        while True:
            self.draw_game()
            self.handle_input()
