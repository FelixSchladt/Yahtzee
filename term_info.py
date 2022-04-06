import os
import platform

def terminal():
    if platform.system() == 'Linux':
        return linux()
    else:
        return windows()

class linux:
    def __init__(self):
        import sys, tty, termios
        self.term_size()

    def term_size(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.rows, self.columns = int(rows), int(columns)
        """

        self.lines < 40 or self.columns < 90:
             self.invalid_terminal_size()
        """
        #TODO implement minimum terminal size

    def invalid_terminal_size(self):
        pass
        #TODO

    def getch(self):
        import termios, sys, tty
        old_settings = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
        return ch

class windows:
    def __init__(self):
        import msvcrt

    def getch(self):
        return msvcrt.getch()

if __name__ == "__main__":
    term = terminal()
    print(term.getch())
