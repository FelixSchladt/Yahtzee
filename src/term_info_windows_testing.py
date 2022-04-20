#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)
# add the functions for windows
import os
import platform
import shutil

if platform.system() == 'Linux':
    import sys, tty, termios
else:
    import msvcrt


def terminal():
    if platform.system() == 'Linux':
        return _linux()
    else:
        return _windows()


class _linux:
    def __init__(self):
        self.rows, self.columns = self.term_size()

    def term_size(self):
        with os.popen('stty size', 'r') as pipe:
            rows, columns = pipe.read().split()

        return int(rows) - 1, int(columns)

    def invalid_terminal_size(self):
        pass
        # TODO implement watch function which checks for changing termianl size

    def getch(self):
        old_settings = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
        return ch

    def exit_raw(self):
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)


class _windows:
    def __init__(self):
        self.lines, self.columns = self.term_size()

    def term_size(self):
        columns, lines = shutil.get_terminal_size()
        return int(columns), int(lines)

    def getch(self):
        return msvcrt.getch()

    def invalid_terminal_size(self):
        pass
        # TODO implement watch function which checks for changing termianl size


#if __name__ == "__main__":
#    term = terminal()
#    print(term.getch())