#!usr/bin/python3
# pylint: disable=C

# Copyright 2022 Ginthom (https://github.com/GinThom)

from unittest import TestCase

from src.dices import dice as Dice
from src.dices import get_dices


class TestRuleGenerator(TestCase):
    def test_get_dices(self):
        self.assertIsNotNone(get_dices()) 

    def test_dice(self):
        test_dice = Dice()
        self.assertIsInstance(test_dice, Dice)

    def setUp(self):
        self.dice = Dice()

    def test_dice_roll(self):
        for _ in range(0, 10):
            self.assertIn(self.dice.roll(), range(1, 7))

    def tearDown(self):
        pass
