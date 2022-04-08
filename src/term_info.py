#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

import os
import platform

if platform.system() == 'Linux' or platform.system() == 'FreeBSD':
    import sys, tty, termios
else:
    import msvcrt
    import shutil

def terminal():
    """
    returns the platform specific library for terminal handling
    """
    if platform.system() == 'Linux' or platform.system() == 'FreeBSD':
        return _posix()
    else:
        return _windows()

class _posix:
    """
    handles platform specific terminal functionality for posix conforment systems
    """
    def __init__(self):
        self.rows, self.columns = self.term_size()

    def term_size(self):
        """
        returns current size and height of terminal in characters
        """
        with os.popen('stty size', 'r') as pipe:
            rows, columns = pipe.read().split()

        return int(rows)-1, int(columns)

    def invalid_terminal_size(self):
        """
        Checks for minimum required size
        """
        pass
        #TODO implement watch function which checks for changing termianl size

    def getch(self):
        """
        sets terminal to raw mode in order to be able to get raw keyboard input
        """
        self.old_settings = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.old_settings)
        return ch

    def exit_raw(self):
        """
        Reverts env to normal mode / clean up function
        """
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, self.old_settings)


# TODO  I read that the colorama module is needed at least in the ancient dos box terminal, but since win11/win10 i belive ther is a new terminal available
#       Please check if ansi escape sequences work in this and colored text and cursor positioning works as excpected

class _windows:
    """
    handles platform specific terminal functionality for nt based systems
    """
    def __init__(self):
        self.lines, self.columns = self.term_size()

    @staticmethod
    def getch():
        """
        uses msvcrt library to get character input
        """
        return msvcrt.getch()

    def term_size(self):
        """
        returns current size and height of terminal in characters
        """
        columns, lines = shutil.get_terminal_size()
        return int(columns), int(lines)

    def invalid_terminal_size(self):
        """
        Checks for minimum required size
        """
        #TODO implement watch function which checks for changing termianl size
        pass

    @staticmethod
    def exit_raw():
        """
        Placeholder to ensure compatibility
        """
        pass


if __name__ == "__main__":
    term = terminal()
    print(term.getch())
