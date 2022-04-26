#!/usr/bin/python3

# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

"""
Library for displaying dynamic content in the commandline
"""
from src.exceptions import InvalidLenghtError, OutOfBoundsError
from src.term_info import terminal, Colors
from src.rules import CATEGORIES

#OFFSET for the Score table and WIDTH for the Value Tables
OFFSET = 90

MIN_HEIGHT = 38
MIN_WIDTH  = 123

chars = {
    'a': '┌',
    'b': '┐',
    'c': '┘',
    'd': '└',
    'e': '─',
    'f': '│',
    'g': '┴',
    'h': '├',
    'i': '┬',
    'j': '┤',
    'k': '╷',
    'l': '┼',
}




class TuiEngine:
    """
    Creates a virtual display in the terminal by using assign each character
    a coordinate
    """
    __dice =   {1: ["     ", "  *  ", "     "],
                2: ["     ", " * * ", "     "],
                3: [" *   ", "  *  ", "   * "],
                4: [" * * ", "     ", " * * "],
                5: [" * * ", "  *  ", " * * "],
                6: [" * * ", " * * ", " * * "]}

    def __init__(self):
        self.terminal = terminal()
        self.__grid_init()
        self.display_width = self.terminal.columns -1
        self.display_height = self.terminal.rows -1

    def __grid_init(self):
        self.__grid = [[" " for j in range(self.terminal.columns)]\
                for i in range(self.terminal.rows+1)]

    def invalid_terminal_size(self):
        '''Check if the dimensions of the current terminal fit the minimum
           requirements of the game
        '''
        if self.display_width < MIN_WIDTH  or self.display_height < MIN_HEIGHT:
            raise OutOfBoundsError

    def reset_grid(self):
        """
        creates new empty grid buffer
        """
        self.__grid_init()

    def flush(self):
        """
        prints grid buffer onto terminal
        """
        for counter, value in enumerate(self.__grid):
            # TODO Check if this works on WINDOWS -> if not is colorama needed?
            # Refer to comment in term_info.py at _windows class
            # ====> I implemented a supposed fix working for windos 10 and
            #       newer in term_info.py bitte testen
            print(f"\033[{counter};0H" + "".join(value))

    def pixel(self, pos_x, pos_y, char = " ", color = ""):
        """
        assigns char to (pos_x, pos_y) coordinate in the grid buffer
        """
        if len(char) != 1:
            raise InvalidLenghtError
        if len(self.__grid) < (pos_y+1) or len(self.__grid[0]) < pos_x:
            raise OutOfBoundsError
        self.__grid[pos_y+1][pos_x] = f"{color}{char}{Colors.END}"

    def text(self, pos_x, pos_y, txt, length=None, color = ""):
        """
        prints text into the grid buffer
        Starts at (pos_x, pos_y) coordinate.
        If a length is specified, no symbols beyond the lenght will be written
        """
        txt = str(txt)
        length = len(txt) if length is None else length

        if (length + pos_x) > self.display_width:
            raise OutOfBoundsError

        if length > len(txt):
            length = len(txt)

        i = 0
        for x_0 in range(pos_x, pos_x + int(length)):
            self.pixel(x_0, pos_y, txt[i], color)
            i+=1

    def frame(self, x_0 = 0, y_0 = 0, x_1 = None, y_1 = None):
        """
        draws a solid lined broder around the specified coordinates
        """
        x_1 = self.display_width if x_1 is None else x_1
        y_1 = self.display_height if y_1 is None else y_1

        self.line_horizontal(y_0, x_0, x_1, char = "─")
        self.line_horizontal(y_1, x_0, x_1, char = "─")

        self.line_vertical(x_0, y_0, y_1, char = "│")
        self.line_vertical(x_1, y_0, y_1, char = "│")

        self.pixel(x_0, y_0, "┌")
        self.pixel(x_0, y_1, "└")
        self.pixel(x_1, y_0, "┐")
        self.pixel(x_1  , y_1, "┘")


    def dice(self, x_pos, y_pos, face):
        """
        prints ascii representation of an dice to (x_pos, y_pos) top left
        """
        self.frame(x_pos, y_pos, x_pos + 6, y_pos + 4)
        for counter, text in enumerate(self.__dice[face]):
            self.text(x_pos + 1, y_pos + counter + 1, text)

    def line_horizontal(self, pos_y, x_0 = 0, x_1 = None, char = " ", color = ""):
        """
        Draws line from (x_0, pos_y) to (x_1, pos_y)
        """
        x_1 = self.display_width if x_1 is None else x_1
        for pos_x in range(
                x_0 if x_0 < x_1
                else x_1,
                x_1 if x_0 < x_1
                else x_0):
            self.pixel(pos_x, pos_y, char, color)

    def line_vertical(self, pos_x, y_0 = 0, y_1 = None, char = " ", color = ""):
        """
        Draws line from (pos_x, y_0) to (pos_x, y_1)
        """
        y_1 = self.display_height if y_1 is None else y_1
        for pos_y in range(
                y_0 if y_0 < y_1
                else y_1,
                y_1 if y_0 < y_1
                else y_0):
            self.pixel(pos_x, pos_y, char, color)

    def rectangle(self, x_pos, y_pos, width, height, char = " ", color = ""):
        """
        Fills a rectangular section with char on the grid
        """
        for i in range(height):
            self.line_horizontal(y_pos + i, x_pos, x_pos + width, char, color)

    def draw_table(self, x_pos, y_pos, width, height, left="├"):
        """
        Draws a table and return a list with objects to assign text to the columns
        Table is only one column wide -> if multiple columns are needed place the
        tables next to each other and pass '┼' as left parameter
        """
        self.frame(x_pos, y_pos, x_pos + width, y_pos + height)

        for i in range(y_pos+2, y_pos+height, 2):
            self.line_horizontal(i, x_pos, x_pos+width, "─")
            self.pixel(x_pos, i, left)
            self.pixel(x_pos+width, i, "┤" )

        if left == "┼":
            self.pixel(x_pos, y_pos, "┬")
            self.pixel(x_pos, y_pos + height, "┴")

        return [ PlacedText(self, x_pos+1, j, width-2) for j in range(y_pos+1, y_pos+height, 2)]



class PlacedText:
    """
    Text field with given coordinates and lenght
    """
    def __init__(self, tui, x_pos, y_pos, length):
        self.tui = tui
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length

    def __call__(self, text, color = ""):
        self.tui.text(self.x_pos, self.y_pos, text, self.length)

class RoundsBox:
    '''A dedicated class to display a box containing the remaining rounds
    '''
    def __init__(self, tui):
        self.rounds = 3
        self.__tui = tui
        self.text = PlacedText(tui, 57, 4, 30)
        self.draw()

    def draw(self):
        '''Draws the box

           :returns: None
        '''
        self.__tui.frame(55, 3, 77, 5)
        self.text(f"Rounds remaining: {self.rounds}")

    def set_round(self, rounds: int):
        '''Set the displayed round
        '''
        self.rounds = rounds

    def reset(self):
        '''Reset the counter in the box
        '''
        self.rounds = 3
        self.draw()

    def __call__(self):
        self.rounds -= 1
        if self.rounds == 0:
            self.reset()
            return False
        self.draw()
        return True


def category_table(tui):
    """
    Draws table with the yathzee categories
    """
    fields = tui.draw_table(tui.display_width - OFFSET , 2, 17, 17 *2)
    for counter, field in enumerate(fields):
        field(CATEGORIES[counter])

def update_player_scores(players):
    '''Get both players current scores

       :param players: the players whos scores are supposed to be
                       displayed
       :returns: None
    '''
    for player in players:
        for i in range(len(CATEGORIES)):
            player.table[i](player.scores[i])
        player.table[0](player.name)
        player.calculate_scores()


def draw_player_tables(tui, players):
    """
    Draws tables for the players points
    """
    w_1, w_2 = len(players[0].name), len(players[1].name)
    players[0].table = tui.draw_table(tui.display_width - OFFSET + 17, 2, w_1+2, 17 *2, "┼")
    players[1].table = tui.draw_table(tui.display_width - OFFSET + 17 + w_2+2, 2, w_2+2, 17 *2, "┼")

    update_player_scores(players)


def draw_dices(tui, dices):
    '''Draws all dices in the terminal

       :param tui: The drawing engine
       :param dices: The dices to be drawn
       :returns: Non None
    '''
    gap_size = 2
    dice_width = 7 + gap_size
    dice_height = 5

    for counter, dice in enumerate(dices):
        level_1, level_2  = (2*dice_height, 2) if dice.selected else (2, 2*dice_height)
        x_pos, y_pos = [(4+counter*dice_width, level_1,) for i in range(5)][counter]
        tui.dice(x_pos, y_pos, dice.value)
        tui.rectangle(x_pos, level_2, dice_width, dice_height, )


def log(msg):
    '''Log function for the drawing engine

       :param msg: the log message
       :returns: None
    '''
    with open("tui_engine.log", "a", encoding='utf-8') as myfile:
        myfile.write(msg + "\n")
