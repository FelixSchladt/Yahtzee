#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

import os
import platform

if platform.system() == 'Linux' or platform.system() == 'FreeBSD':
    import sys, tty, termios
else:
    import msvcrt
    import shutil
    import ctypes

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

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

    @staticmethod
    def clear():
        """
        clears output in the terminal
        """
        os.system("clear")

# TODO  I read that the colorama module is needed at least in the ancient dos box terminal, but since win11/win10 i belive ther is a new terminal available
#       Please check if ansi escape sequences work in this and colored text and cursor positioning works as excpected

class _windows:
    """
    handles platform specific terminal functionality for nt based systems
    """
    def __init__(self):
        self.rows, self.columns = self.term_size()
        #TODO Should enable ANSI codes in cmd on windows without colorama
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    @staticmethod
    def getch():
        """
        uses msvcrt library to get character input
        """
        return msvcrt.getch()

    @staticmethod
    def clear():
        """
        clears output in the terminal
        """
        os.system("cls")

    def term_size(self):
        """
        returns current size and height of terminal in characters
        """
        columns, rows = shutil.get_terminal_size()
        return int(columns), int(rows)

    @staticmethod
    def exit_raw():
        """
        Placeholder to ensure compatibility
        """
        pass


if __name__ == "__main__":
    term = terminal()
    print(ord(term.getch()))
    for i in dir(Colors):
        if i[0:1] != "_" and i != "END":
            print("{:>16} {}".format(i, getattr(Colors, i) + i + Colors.END))
