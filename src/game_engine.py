#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)
# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

'''This module contains the games main loop
   and general controll unit
'''

import sys
import os
from json import JSONDecodeError
from time import sleep
from src.tui_engine import TuiEngine,\
                           RoundsBox,\
                           draw_dices,\
                           draw_player_tables,\
                           category_table,\
                           log
from src.player import new_players
from src.rules import CATEGORIES, CATEGORY_FUNCTIONS
from src.terminal import Colors
from src.exceptions import OutOfBoundsError
from src.file_handler import save, load


class GameEngine():
    '''The main backend of the game
    '''
    def __init__(self, save_file: str = None, player_two: str = None, player_one: str = None):
        players = [ player if player is not None else f"Player{counter+1}" for\
                   counter, player in enumerate( (player_one, player_two) ) ]

        save_file = "save" if save_file is None else save_file

        self.tui = TuiEngine()

        self.round_box = None #Can throw not catchable OutOFBoundsError if terminal
        #size is too small too initialize the box #RoundsBox(self.tui)
        self.turns = 3

        self.height, self.width = self.tui.terminal.term_size()
        self.save_path = save_file.replace(".json", "")

        if os.path.exists(self.save_path):
            try:
                # TODO this doesnt work
                self.load_game()

            except (JSONDecodeError, ValueError):
                self._init_players(*players)

        else:
            self._init_players(*players)

    def _init_players(self, name_one: str, name_two: str):
        self.players = new_players(name_one, name_two)

    def _validate_save_file_contents(self, content: {}):
        '''This method checks whether the data found in a save file matches
           the format used by the game.

           :throws: ValueError, when data is invalid
           :returns: None
        '''
        # TODO implement this#

    def getch(self):
        """
            This method checks if terminal size has changed and if so does
            reinitialize tui_engine -> if nothing changes, it just proceeds to return
            the blocking terminal.getch() of terminal object
        """
        current_height, current_width = self.tui.terminal.term_size()
        if self.height != current_height or self.width != current_width:
            self.height, self.width = current_height, current_width

            self.tui.reset_grid()
        self.tui.invalid_terminal_size()
        return self.tui.terminal.getch()

    def invalid_screen_size(self):
        """This function shows the screen if the current terminal size is too small
        """
        self.tui = TuiEngine()
        text = "Invalid Terminal Size", "Please enlarge the terminal"
        if self.tui.display_height < 4 or self.tui.display_width < (len(max(text, key=len))+4):
            print("Error: Terminal too small")
        else:
            self.tui.text((int(self.tui.display_width/2 - len(text[0])/2),
                      int(self.tui.display_height/2)),
                      text[0],
                      color=Colors.RED)
            self.tui.text((int(self.tui.display_width/2 - len(text[1])/2),
                      int(self.tui.display_height/2+1)),
                      text[1])
            self.tui.flush()
            self.tui.rectangle((2, int(self.tui.display_height/2)),
                           (len(max(text, key = len)), 2))
            sleep(0.1)


    def load_game(self):
        '''This method loads a save state from a save file
           if a save file is given
        '''
        save_dict = load(self.save_path)
        self.turns = save_dict["turns"]
        for i, _ in enumerate(self.players):
            self.players[i].load_from_dict(save_dict[f"players_{i}"])

    def save_game(self):
        '''Stores the game in a save file
        '''
        player_dict = {"turns": self.turns}
        for index, player in enumerate(self.players):
            player_dict[f"player_{index}"] = {"name": player.name,\
                                              "dices": [dice.value for dice in player.dices],\
                                              "flags": list(player.used_rules),\
                                              "scores": list(player.scores)}

        save(player_dict, self.save_path)

    def handle_input(self):
        '''This method is resposible for executing the
           correct methods after a certain key is pressed

           :returns: None
        '''
        key = self.getch()

        if key.isnumeric() and int(key) in range(1, 6):
            active = self.get_active_player_index()
            self.players[active].dices[int(key)-1].switch()

        elif key == 'q':
            self.tui.terminal.clear()
            sys.exit(0)

        elif ord(key) == 13: # 'Enter'
            self.end_turn()

        elif ord(key) == 32: # 'Space'
            self.roll_dice()

        log(f"Input read: {key}")

    def win_screen(self):
        """Screen for showing results o the game"""
        self.tui.terminal.clear()

        p_1, p_2 = ( (player.name, player.get_score()) for player in self.players )

        player_res = (p_1, p_2) if p_1[1] > p_2[1] else (p_2, p_1)

        text = f"Player {player_res[0][0]} won!"

        self.tui.frame(int(self.tui.display_width/2 - len(text)-1), 3,
                       int(self.tui.display_width/2 + len(text)+1), 5)

        self.tui.text((int(self.tui.display_width/2 - len(text)/2), 4), text,
                      color = f"{Colors.BOLD}{Colors.UNDERLINE}")


        len_p1, len_p2 = len(self.players[0].name), len(self.players[1].name)
        player1_fields = self.tui.draw_table((int(self.tui.display_width/2 - len_p1 -2 ),
                                              8), len_p1 +2, 4 )


        player2_fields = self.tui.draw_table((int(self.tui.display_width/2), 8),
                                             len_p2 +2, 4, "┼")



        player1_fields[0](player_res[0][0], color= Colors.GREEN)
        player2_fields[0](player_res[1][0])

        player1_fields[1](player_res[0][1], color= Colors.GREEN)
        player2_fields[1](player_res[1][1])

        text = "Press any key to close the application"
        self.tui.text((int(self.tui.display_width/2 - len(text)/2),
                       self.tui.display_height), text, color = Colors.BOLD)

        self.tui.flush()
        self.getch()
        self.tui.terminal.clear()
        sys.exit(0)

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

        if self.game_over():
            self.tui.terminal.clear()
            self.win_screen()

        self.turns = 3
        self.save_game()

    def select_rule(self):
        '''This method lets the player select the rule he wants to
           collect points for at the end of his turn

           :returns:
        '''
        active = self.get_active_player_index()
        options = self.players[active].get_options()
        selection = -1

        self.tui.terminal.clear()
        print(f"{self.players[active].name} chooses an option:")
        for i, option in enumerate(options):
            print(f"{i+1}. {option[0].upper()}\tPoints: {option[1]}")

        while True:
            try:
                selection = int(input(f"Input (1-{len(options)}): "))- 1

                if not selection in range(len(options)):
                    print("Invalid input, try again!")
                    continue
                break

            except ValueError:
                print("Invalid input, try again!")
                continue

        # Get indices required to read and write the correct
        # results to the player object
        selected_option = options[selection][0]
        formated_option = selected_option.lower().replace(' ', '_')

        scoreboard_index = [ i for i in range(len(CATEGORIES))\
                         if CATEGORIES[i] == selected_option ][0]
        function_index = [ i for i in range(len(CATEGORY_FUNCTIONS))\
                         if formated_option == CATEGORY_FUNCTIONS[i].__name__ ][0]

        # Set player score[index] to correct score
        self.players[active].scores[scoreboard_index] += CATEGORY_FUNCTIONS[function_index](
                self.players[active].get_all_dice_faces())[1]

        self.players[active].used_rules[function_index] = True

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
        self.round_box = RoundsBox(self.tui)
        self.round_box.set_round(self.turns)

        draw_dices(self.tui, self.players[active].dices)
        category_table(self.tui)
        draw_player_tables(self.tui, self.players)
        self.round_box.draw()
        self.tui.text((4, 18), f"Player: {self.players[self.get_active_player_index()].name}"\
                "                ")
        self.tui.text((4, 20), "Selected                  ")
        self.tui.text((4, 20), "Selected: "\
                f"{self.players[active].get_selected_dice_faces()}")
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
            try:
                self.tui.invalid_terminal_size()
                self.draw_game()
                self.handle_input()
            except OutOfBoundsError:
                self.invalid_screen_size()
