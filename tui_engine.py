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
    def __init__(self):
        self.terminal = terminal()
        self.__grid_init()
        self.display_width = self.terminal.columns -1
        self.display_height = self.terminal.rows -1

    def __grid_init(self):
        self.__grid = [[" " for j in range(self.terminal.columns)] for i in range(self.terminal.rows+1)]

    def clear(self):
        """
        clears output in the terminal
        """
        self.__grid_init()

    def flush(self):
        """
        prints grid buffer onto terminal
        """
        #TODO Check if this works on WINDOWS
        for counter, value in enumerate(self.__grid):
            print(f"\033[{counter};0H" + "".join(value))

    def pixel(self, x, y, char = " "):
        """
        assigns char to (x, y) coordinate in the grid buffer
        """
        if len(char) != 1:
            raise InvalidLenght
        if len(self.__grid) < (y+1) or len(self.__grid[0]) < x:
            raise OutOfBounds
        self.__grid[y+1][x] = char

    def text(self, x, y, txt, length=None):
        """
        prints text into the grid buffer
        Starts at (x, y) coordinate.
        If a length is specified, no symbols beyond the lenght will be written
        """
        lenght = len(txt) if length is None else length

        if (lenght + x) > self.display_width:
            raise OutOfBounds

        i = 0
        for x0 in range(x, x + int(lenght)):
            self.pixel(x0, y, txt[i])
            i+=1

    def frame(self, x0 = 0, y0 = 0, x1 = None, y1 = None):
        """
        clears output in the terminal
        """
        x1 = self.display_width if x1 is None else x1
        y1 = self.display_height if y1 is None else y1

        self.line_horizontal(y0, x0, x1, color = "─")
        self.line_horizontal(y1, x0, x1, color = "─")

        self.line_vertical( x0, y0, y1, color = "│")
        self.line_vertical( x1, y0, y1, color = "│")

        self.pixel(x0, y0, "┌")
        self.pixel(x0, y1, "└")
        self.pixel(x1, y0, "┐")
        self.pixel(x1, y1, "┘")

    @staticmethod
    def finish():
        """
        clears output in the terminal
        """
        #TODO Check if this works on WINDOWS
        os.system("clear")

    def line_horizontal(self, y, x0 = 0, x1 = None, color = " "):
        """
        Draws line from (x0, y) to (x1, y)
        """
        x1 = self.display_width if x1 is None else x1
        for x in range(x0 if x0 < x1 else x1, x1 if x0 < x1 else x0):
            self.pixel(x, y, color)

    def line_vertical(self, x, y0 = 0, y1 = None, color = " "):
        """
        Draws line from (x, y0) to (x, y1)
        """
        y1 = self.display_height if y1 is None else y1
        for y in range(y0 if y0 < y1 else y1, y1 if y0 < y1 else y0):
            self.pixel(x, y, color)


if __name__ == "__main__":
    tui = TuiEngine()
    for k in range(0, 10):
        tui.clear()
        #tui.line_vertical(10+i, color = tui.terminal.getch())
        #tui.circle(color = tui.terminal.getch())
        tui.frame()
        tui.frame(10, 10, 30, 30)
        tui.text(12, 12, chr(65 + k))
        tui.flush()
        tui.terminal.getch()
    tui.finish()
