#!/usr/bin/python3

# Copyright 2022 Jannik Künstler (https://github.com/multiinside)

'''The main file of the project
   Run this file to start the game
'''

from src.game_engine import GameEngine
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Basic settings for your Kniffel game')
    parser.add_argument('--savefile', type=str)
    parser.add_argument('--player-one', type=str)
    parser.add_argument('--player-two', type=str)
    GameEngine(*vars(parser.parse_args()).values()).run()
