#!/usr/bin/python3
# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

# pylint: disable=C

import os.path
from unittest import TestCase, expectedFailure
from src.tui_engine import TuiEngine, category_table, OFFSET, log, draw_dices, RoundsBox
from src.dices import get_dices

class TestTuiEngine(TestCase):
    def setUp(self):
        self.tui = TuiEngine()

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

    @expectedFailure
    def test_dice(self):
        self.tui.reset_grid()
        self.tui.dice(0,0,7)

    def test_text(self):
        self.tui.reset_grid()
        self.tui.text((0,0), "test", 3)
        self.assertEqual(self.tui._TuiEngine__grid[1][3], " ")

    @expectedFailure
    def test_OutOfBounds(self):
        self.tui.pixel(0, 99999999999999)

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
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()
        self.assertEqual(last_line, "Test\n")

    def tearDown(self):
        pass
