#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

"""
Library for displaying dynamic content in the commandline
"""

import os
from exceptions import InvalidLenght, OutOfBounds
from term_info import terminal

#OFFSET for the Score table and WIDTH for the Value Tables
OFFSET = 40

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
            print(f"\033[{counter};0H" + "".join(value))

    def pixel(self, pos_x, pos_y, char = " "):
        """
        assigns char to (pos_x, pos_y) coordinate in the grid buffer
        """
        if len(char) != 1:
            raise InvalidLenght
        if len(self.__grid) < (pos_y+1) or len(self.__grid[0]) < pos_x:
            raise OutOfBounds
        self.__grid[pos_y+1][pos_x] = char

    def text(self, pos_x, pos_y, txt, length=None):
        """
        prints text into the grid buffer
        Starts at (pos_x, pos_y) coordinate.
        If a length is specified, no symbols beyond the lenght will be written
        """
        length = len(txt) if length is None else length

        if (length + pos_x) > self.display_width:
            raise OutOfBounds

        if length > len(txt):
            length = len(txt)

        i = 0
        for x_0 in range(pos_x, pos_x + int(length)):
            self.pixel(x_0, pos_y, txt[i])
            i+=1

    def frame(self, x_0 = 0, y_0 = 0, x_1 = None, y_1 = None):
        """
        draws a solid lined broder around the specified coordinates
        """
        x_1 = self.display_width if x_1 is None else x_1
        y_1 = self.display_height if y_1 is None else y_1

        self.line_horizontal(y_0, x_0, x_1, color = "─")
        self.line_horizontal(y_1, x_0, x_1, color = "─")

        self.line_vertical(x_0, y_0, y_1, color = "│")
        self.line_vertical(x_1, y_0, y_1, color = "│")

        self.pixel(x_0, y_0, "┌")
        self.pixel(x_0, y_1, "└")
        self.pixel(x_1, y_0, "┐")
        self.pixel(x_1  , y_1, "┘")



    @staticmethod
    def clear():
        """
        clears output in the terminal
        """
        # TODO Check if this works on WINDOWS
        os.system("clear")

    def dice(self, x_pos, y_pos, face):
        """
        prints ascii representation of an dice to (x_pos, y_pos) top left
        """
        self.frame(x_pos, y_pos, x_pos + 6, y_pos + 4)
        for counter, text in enumerate(self.__dice[face]):
            self.text(x_pos + 1, y_pos + counter + 1, text)

    def line_horizontal(self, pos_y, x_0 = 0, x_1 = None, color = " "):
        """
        Draws line from (x_0, pos_y) to (x_1, pos_y)
        """
        x_1 = self.display_width if x_1 is None else x_1
        for pos_x in range(
                x_0 if x_0 < x_1
                else x_1,
                x_1 if x_0 < x_1
                else x_0):
            self.pixel(pos_x, pos_y, color)

    def line_vertical(self, pos_x, y_0 = 0, y_1 = None, color = " "):
        """
        Draws line from (pos_x, y_0) to (pos_x, y_1)
        """
        y_1 = self.display_height if y_1 is None else y_1
        for pos_y in range(
                y_0 if y_0 < y_1
                else y_1,
                y_1 if y_0 < y_1
                else y_0):
            self.pixel(pos_x, pos_y, color)

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
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})

    def __call__(self, text):
        self.tui.text(self.x_pos, self.y_pos, text, self.length)


def category_table(tui):
    """
    Draws table with the yathzee categories
    """
    categories =["", "Aces", "Twos", "Threes", "Fours", "Fives", "Sixes", "Total ->",\
                "Bonus if t > 63", "Three Of A Kind", "Four Of A Kind", "Full House",\
                "Small Straight", "Large Straight", "Yahtzee", "Chance", "Total"]

    fields = tui.draw_table(tui.display_width - OFFSET , 2, 17, 17 *2)
    for counter, field in enumerate(fields):
        field(categories[counter])

def draw_player_tables(tui, name_1 = "Player1", name_2 = "Player2"):
    """
    Draws tables for the players points
    """
    w_1, w_2 = len(name_1), len(name_2)
    player_1 = tui.draw_table(tui.display_width - OFFSET + 17, 2, w_1+2, 17 *2, "┼")
    player_2 = tui.draw_table(tui.display_width - OFFSET + 17 + w_2+2, 2, w_2+2, 17 *2, "┼")

    player_1[0](name_1)
    player_2[0](name_2)

    return player_1, player_2


if __name__ == "__main__":
    tui = TuiEngine()
    for k in range(1, 7):
        tui.clear()
        tui.frame()
        tui.text(12, 12, "te" )
        category_table(tui)
        draw_player_tables(tui)
        #tui.frame(10, 10, 30, 30)
        #tui.text(12, 12, chr(65 + k))
        #tui.dice(40, 10, k)
        tui.flush()
        tui.terminal.getch()
    tui.clear()
