#!/usr/bin/python3
# Copyright 2022 FelixSchladt (https://github.com/FelixSchladt)

# pylint: disable=C

from unittest import TestCase
from src.tui_engine import TuiEngine


class TestTuiEngine(TestCase):
    def setUp(self):
        self.tui = TuiEngine()


    def test_pixel(self):
        self.tui.pixel(0,0, "A")
        self.assertEqual(self.tui._TuiEngine__grid[1][0], "A")

