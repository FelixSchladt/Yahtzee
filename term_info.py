import os
import platform

def terminal():
    if platform.system() == 'Linux':
        return _linux()
    else:
        return _windows()

class _linux:
    def __init__(self):
        import sys, tty, termios
        self.rows, self.columns = self.term_size()

    def term_size(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        return int(rows), int(columns)

    def invalid_terminal_size(self):
        pass
        #TODO implement watch function which checks for changing termianl size

    def getch(self):
        import termios, sys, tty
        old_settings = termios.tcgetattr(sys.stdin.fileno())
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
        return ch


class _windows:
    def __init__(self):
        import msvcrt

    def getch(self):
        return msvcrt.getch()

    def term_size():
        #TODO implement working windows version
        pass

    def invalid_terminal_size(self):
        pass
        #TODO implement watch function which checks for changing termianl size


if __name__ == "__main__":
    term = terminal()
    print(term.getch())
