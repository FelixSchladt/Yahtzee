#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

# pylint: disable=C

from unittest import TestCase
from json import JSONDecodeError
from src.game_engine import GameEngine

class TestRuleGenerator(TestCase):
    def setUp(self):
        self.engine = GameEngine(player_one = "Player One",
                                 player_two = "Players Two")
        self.correct_file = "./test/save_files/correct"
        self.faulty_json_file = "./test/save_files/faulty_format"
        self.corrupted_file = "./test/save_files/corrupted"

    def test_load_game_correct(self):
        self.engine.save_path = self.correct_file
        # Check for some values to be correct as 
        # checking for ALL of them would be overkill
        self.assertTrue(len(self.engine.players) == 2)
        self.assertTrue(len(self.engine.players[0].dices) == 5)
        self.assertTrue(self.engine.turns == 3)
        self.assertTrue(len(self.engine.players[1].used_rules) == 13)

    def test_load_game_faulty_format(self):
        self.engine.save_path = self.faulty_json_file
        self.assertRaises(JSONDecodeError, self.engine.load_game)

    def test_load_game_faulty_data(self):
        self.engine.save_path = self.corrupted_file
        # Error is dependent on what part of the file is corrupted
        self.assertRaises((ValueError, KeyError), self.engine.load_game)

