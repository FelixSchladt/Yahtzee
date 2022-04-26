#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

'''The main file of the project
   Run this file to start the game
'''

from src.game_engine import GameEngine
import argparse

def main():
    """
    Create Arguments "--name_one", "--name_two", "savefile" for starting the game
    """
    parser_name = argparse.ArgumentParser(description='Set player names')
    parser_name.add_argument('--name_one', type=str)
    parser_name.add_argument('--name_two', type=str)
    args_name = parser_name.parse_args()

    parser_savefile = argparse.ArgumentParser(description='Load a savefile')
    parser_savefile.add_argument('--savefile', type=int)
    args_savefile = parser_savefile.parse_args()

if __name__ == '__main__':
    GameEngine().run()
