#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

# pylint: disable=C

from unittest import TestCase, expectedFailure
from src.tui_engine import TuiEngine


class TestTuiEngine(TestCase):
    def setUp(self):
        self.tui = TuiEngine()

    def test_pixel(self):
        #self.tui = TuiEngine()
        self.tui.pixel(0,0, "A")
        self.assertEqual(self.tui._TuiEngine__grid[1][0], "A")

    def test_frame(self):
        self.tui.reset_grid()
        self.tui.frame(1, 1, 4, 4)
        self.assertEqual(self.tui._TuiEngine__grid[2][1], "┌")
        self.assertEqual(self.tui._TuiEngine__grid[2][4], "┐")
        self.assertEqual(self.tui._TuiEngine__grid[5][1], "└")
        self.assertEqual(self.tui._TuiEngine__grid[5][4], "┘")

    @expectedFailure
    def test_dice(self):
        self.tui.reset_grid()
        self.tui.dice(0,0,7)

    def test_text(self):
        self.tui.reset_grid()
        self.tui.text(0,0, "test", 3)
        self.assertEqual(self.tui._TuiEngine__grid[1][3], " ")

    @expectedFailure
    def test_OutOfBounds(self):
        self.tui.pixel(0, 9999999999999999999999)

    def tearDown(self):
        pass
