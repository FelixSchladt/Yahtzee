#!/usr/bin/python3
# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

# pylint: disable=C

import os.path
from unittest import TestCase, expectedFailure
from unittest.mock import patch
from src.tui_engine import TuiEngine, category_table, OFFSET, log, draw_dices, RoundsBox
from src.dices import get_dices
from src.exceptions import OutOfBoundsError

class TestTuiEngine(TestCase):
    def setUp(self):
        self.tui = TuiEngine()
        self.do_nothing = lambda *args, **kwargs:\
                          lambda *args, **kwargs: None

    def test_invalid_terminal_size_invalid_size(self):
        self.tui.display_width = 1
        self.tui.display_height = 1
        with patch('src.tui_engine.TuiEngine.__init__', new_callable=self.do_nothing),\
             self.assertRaises(OutOfBoundsError) as err:
            self.tui.invalid_terminal_size()

        self.assertIsInstance(err.exception, OutOfBoundsError)

    def test_invalid_terminal_size(self):
        with patch.object(TuiEngine, '__init__') as mock_init:
            self.tui.invalid_terminal_size()
            mock_init.assert_called_with()
    
    def test_pixel(self):
        self.tui.pixel(0,0, "A")
        self.assertEqual(self.tui._TuiEngine__grid[1][0], "A\x1b[0m")

    def test_frame(self):
        self.tui.reset_grid()
        self.tui.frame(1, 1, 4, 4)
        self.assertEqual(self.tui._TuiEngine__grid[2][1], "┌\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[2][4], "┐\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[5][1], "└\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[5][4], "┘\x1b[0m")

    def test_dice(self):
        self.tui.reset_grid()
        with self.assertRaises(KeyError) as err:
            self.tui.dice(0,0,7)

        self.assertIsInstance(err.exception, KeyError)

    def test_text(self):
        self.tui.reset_grid()
        self.tui.text((0,0), "test", 3)
        self.assertEqual(self.tui._TuiEngine__grid[1][3], " ")

    def test_OutOfBounds(self):
        with self.assertRaises(OutOfBoundsError) as err:
            self.tui.pixel(0, 99999999999999)

        self.assertIsInstance(err.exception, OutOfBoundsError)

    def test_category_table(self):
        category_table(self.tui)
        self.assertEqual(self.tui._TuiEngine__grid[36][self.tui.display_width - OFFSET +1], "T\x1b[0m")

    def test_dices(self):
        draw_dices(self.tui, get_dices())
        self.assertEqual(self.tui._TuiEngine__grid[3][4], "┌\x1b[0m")

    def test_roundsbox(self):
        roundbox = RoundsBox(self.tui)
        self.assertEqual(roundbox.rounds, 3)
        roundbox.text("Test")
        self.assertEqual(roundbox.text.text, "Test")


    def test_log(self):
        log("Test")
        with open("tui_engine.log", "rb") as file:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
            last_line = file.readline().decode()
        self.assertEqual(last_line, "Test\n")

    def tearDown(self):
        pass
