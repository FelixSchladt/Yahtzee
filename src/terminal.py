#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

"""
Returns an OS specific object for handleing terminal functionality such as clear,
getch and terminal size
Also contains a class with the ANSI color codes
"""

import os
import platform

if platform.system() == 'Windows':
    import msvcrt
    import shutil
    import ctypes
else:
    #Should work on all Posix compliant systems such as Linux, FreeBsd, Darwin(Not tested)
    import sys
    import tty
    import termios


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
            self.rows, self.columns = pipe.read().split()
        self.rows=int(self.rows)-1
        self.columns = int(self.columns)
        return self.rows, self.columns

    @staticmethod
    def getch():
        """
        sets terminal to raw mode in order to be able to get raw keyboard input
        """
        old_settings = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        char = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
        return char

    @staticmethod
    def clear():
        """
        clears output in the terminal
        """
        os.system("clear")


class _windows:
    """
    handles platform specific terminal functionality for nt based systems
    """
    def __init__(self):
        self.rows, self.columns = self.term_size()
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    @staticmethod
    def getch():
        """
        uses msvcrt library to get character input
        """
        return msvcrt.getch().decode()

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
        self.columns, self.rows = (int(element) for element in shutil.get_terminal_size())
        self.rows-=1
        return self.rows, self.columns


if __name__ == "__main__":
    term = terminal()
    for i in dir(Colors):
        if i[0:1] != "_" and i != "END":
            print(f"{i:>16} {getattr(Colors, i)}{i}{Colors.END}")
