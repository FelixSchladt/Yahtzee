#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

# pylint: disable=C

import os
import json
from unittest        import TestCase
from unittest.mock   import patch
from json            import JSONDecodeError
from src.game_engine import GameEngine
from src.tui_engine  import TuiEngine
from src.dices       import Dice
from src.player      import Player

class TestRuleGenerator(TestCase):
    def setUp(self):
        self.engine = GameEngine(player_one = "Player One",
                                 player_two = "Players Two")
        self.correct_file = "./test/save_files/correct"
        self.faulty_json_file = "./test/save_files/faulty_format"
        self.corrupted_file = "./test/save_files/corrupted"
        self.write_too_file = "./test/save_files/write_tests_here"
        self.do_nothing = lambda *args, **kwargs:\
                          lambda *args, **kwargs: None

    def test_constructor_with_save_path(self):
        test_engine = GameEngine(save_file=self.correct_file)
        self.assertEqual(test_engine.turns, 1)
        self.assertEqual(test_engine.players[0].name, "Thomas")

    def test_constructor_with_save_path_unknown_path(self):
        test_engine = GameEngine(save_file="Some path")
        #Player one is randomly assigned so its either of the two
        self.assertTrue(test_engine.players[0].name in ("Player 1", "Player 2"))
        self.assertTrue(test_engine.players[1].name in ("Player 1", "Player 2"))

    def test_constructor_with_save_path_faulty_file(self):
        test_engine = GameEngine(save_file=self.faulty_json_file)
        self.assertTrue(test_engine.players[0].name in ("Player 1", "Player 2"))
        self.assertTrue(test_engine.players[1].name in ("Player 1", "Player 2"))

    def test_load_game_correct(self):
        self.engine.save_path = self.correct_file
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
        self.assertRaises((ValueError, KeyError, IndexError), self.engine.load_game)

    def test_save_game(self):
        self.engine.save_path = self.write_too_file
        self.engine.save_game()
        self.assertTrue(os.path.isfile(f"{self.write_too_file}.json"))

    def test_getch_valid_size(self):
        with patch('src.terminal._windows.term_size', return_value=(999,999)),\
             patch('src.terminal._windows.getch',     return_value='q'),\
             patch('src.terminal._posix.term_size',   return_value=(999,999)),\
             patch('src.terminal._posix.getch',       return_value='q'):
            result = self.engine.getch()
            self.assertEqual(result, "q")

    def test_getch_invalid_size(self):
        with patch('src.terminal._windows.term_size', return_value=(999,999)),\
             patch('src.terminal._windows.getch',     return_value='q'),\
             patch('src.terminal._posix.term_size',   return_value=(999,999)),\
             patch('src.terminal._posix.getch',       return_value='q'):
            self.engine.height = 100
            self.engine.width  = 100
            result = self.engine.getch()
            self.assertEqual(result, "q")

    def test_invalid_screen_size(self):
        with patch.object(TuiEngine, 'text') as mock,\
             patch('src.tui_engine.TuiEngine.flush', new_callable=self.do_nothing):
            self.engine.invalid_screen_size()
            mock.assert_called_with(((int(self.engine.tui.display_width/2-27/2)),
                int(self.engine.tui.display_height/2+1)),
                "Please enlarge the terminal")

    def test_handle_input(self):
        with patch('src.game_engine.GameEngine.getch', return_value='1'),\
             patch.object(Dice, 'switch') as mock:
            self.engine.handle_input()
            mock.assert_called_with()

        with patch('src.game_engine.GameEngine.getch', return_value=chr(13)),\
             patch.object(GameEngine, 'end_turn') as mock:
            self.engine.handle_input()
            mock.assert_called_with()

        with patch('src.game_engine.GameEngine.getch', return_value=chr(32)),\
             patch.object(GameEngine, 'roll_dice') as mock:
            self.engine.handle_input()
            mock.assert_called_with()

    def test_handle_input_on_exit(self):
        with patch('src.game_engine.GameEngine.getch', return_value='q'),\
             patch.object(GameEngine, 'soft_exit') as mock,\
             patch('src.terminal._windows.clear',      new_callable=self.do_nothing),\
             patch('src.terminal._posix.clear',        new_callable=self.do_nothing):
            self.engine.handle_input()
            mock.assert_called_with()

    def test_win_screen(self):
        with patch('src.tui_engine.TuiEngine.flush',   new_callable=self.do_nothing),\
             patch('src.terminal._windows.clear',      new_callable=self.do_nothing),\
             patch('src.game_engine.GameEngine.getch', return_value='q'),\
             patch('src.terminal._posix.clear',        new_callable=self.do_nothing),\
             self.assertRaises(SystemExit)    as cm:
            self.engine.win_screen()
        self.assertEqual(cm.exception.code, 0)

    def test_end_turn(self):
        with patch('src.game_engine.GameEngine.save_game', new_callable=self.do_nothing),\
             patch('src.terminal._windows.clear',          new_callable=self.do_nothing),\
             patch('src.terminal._posix.clear',            new_callable=self.do_nothing),\
             patch.object(Player, 'calculate_scores') as mock_cs,\
             patch.object(Player, 'get_options')      as mock_go,\
             patch.object(Player, 'reset_dice')       as mock_rd:
            self.engine.end_turn()
            mock_cs.assert_called_with()
            mock_go.assert_called_with()
            mock_rd.assert_called_with()

    def test_end_turn_with_game_over(self):
        with patch('src.game_engine.GameEngine.save_game',  new_callable=self.do_nothing),\
             patch('src.terminal._windows.clear',           new_callable=self.do_nothing),\
             patch('src.terminal._posix.clear',             new_callable=self.do_nothing),\
             patch('src.game_engine.GameEngine.win_screen', new_callable=self.do_nothing),\
             patch('src.game_engine.GameEngine.game_over',  return_value=True),\
             patch.object(Player, 'calculate_scores') as mock_cs,\
             patch.object(Player, 'get_options')      as mock_go,\
             patch.object(Player, 'reset_dice')       as mock_rd,\
             patch.object(GameEngine, 'win_screen')   as mock_ws:
            self.engine.end_turn()
            mock_cs.assert_called_with()
            mock_go.assert_called_with()
            mock_rd.assert_called_with()
            mock_ws.assert_called_with()

    def test_select_rule(self):
        with patch('src.terminal._posix.clear',   new_callable=self.do_nothing),\
             patch('src.terminal._windows.clear', new_callable=self.do_nothing),\
             patch('src.game_engine.GameEngine.get_active_player_index', return_value=True),\
             patch('builtins.print',              new_callable=self.do_nothing),\
             patch('builtins.input',              return_value="1"):
            self.engine.select_rule()
            self.assertTrue(self.engine)

    def test_soft_exit(self):
        with patch('src.terminal._posix.clear',   new_callable=self.do_nothing),\
             patch('src.terminal._windows.clear', new_callable=self.do_nothing),\
             patch('src.game_engine.GameEngine.getch', return_value='y'),\
             self.assertRaises(SystemExit) as cm:
            self.engine.soft_exit()
        self.assertEqual(cm.exception.code, 0)
