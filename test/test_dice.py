#!usr/bin/python3
# pylint: disable=C

# Copyright 2022 Ginthom (https://github.com/GinThom)

from unittest import TestCase

from src.dices import Dice
from src.dices import get_dices, reset_dices


class TestRuleGenerator(TestCase):
    def test_get_dices(self):
        self.assertIsNotNone(get_dices()) 

    def test_dice(self):
        test_dice = Dice()
        self.assertIsInstance(test_dice, Dice)

    def test_reset_dices(self):
        dices = [ Dice() for _ in range(1, 5) ]
        for index, dice in enumerate(dices):
            dice.roll()
            if index % 2 != 0:
                dice.switch()

        reset_dices(dices)
        for dice in dices:
            self.assertFalse(dice.selected)
            self.assertTrue(dice.value in range(1, 7))

    def setUp(self):
        self.dice = Dice()

    def test_dice_roll(self):
        for _ in range(0, 10):
            self.assertIn(self.dice.roll(), range(1, 7))

    def test_dice_switch(self):
        self.assertFalse(self.dice.selected)
        self.dice.switch()
        self.assertTrue(self.dice.selected)
        self.dice.switch()
        self.assertFalse(self.dice.selected)

    def tearDown(self):
        pass
