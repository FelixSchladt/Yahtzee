#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

"""
Library for displaying dynamic content in the commandline
"""

import os
from exceptions import InvalidLenght, OutOfBounds
from term_info import terminal

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
        lenght = len(txt) if length is None else length

        if (lenght + pos_x) > self.display_width:
            raise OutOfBounds

        i = 0
        for x_0 in range(pos_x, pos_x + int(lenght)):
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
        self.pixel(x_1, y_1, "┘")

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


if __name__ == "__main__":
    tui = TuiEngine()
    for k in range(1, 7):
        tui.clear()
        tui.frame()
        tui.frame(10, 10, 30, 30)
        #tui.text(12, 12, chr(65 + k))
        tui.text(12, 12, "test", 2 )
        tui.dice(40, 10, k)
        tui.flush()
        tui.terminal.getch()
    tui.clear()
