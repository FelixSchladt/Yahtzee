#!/usr/bin/python3

# Copyright 2022 Jannik Künstler (https://github.com/multiinside)

'''The main file of the project
   Run this file to start the game
'''

import argparse
import signal
import sys

from src.game_engine import GameEngine
from src.terminal import terminal

def sigint(sig, frame):
    """Callback function for exiting game when SIGINT or SIGKILL
    """
    print(sig, frame) # pylint likes this
    terminal().clear()
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint)

    parser = argparse.ArgumentParser(description='Basic settings for your Kniffel game')
    parser.add_argument('-s', '--savefile', type=str)
    parser.add_argument('-1', '--player-one', type=str)
    parser.add_argument('-2', '--player-two', type=str)

    GameEngine(*vars(parser.parse_args()).values()).run()
