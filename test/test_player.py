#!/usr/bin/python3
# pylint: disable=C

# Copyright 2022 Ginthom (https://github.com/Ginthom)
# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

from unittest import TestCase

from src.player import Player, new_players

class TestRuleGenerator(TestCase):
    def setUp(self):
        self.player = Player("Player One")
        self.max_score = 1535

    def test_calculate_scores(self):
        self.player.calculate_scores()

        result = 0
        for score in self.player.scores:
            result += score

        self.assertTrue(result in range(0, self.max_score))

    def test_get_options(self):
        options = self.player.get_options()

        for option in options:
            self.assertTrue(option[1] in range(0, 51))

    def test_scores(self):
        self.player.scores[6] = 66
        self.player.calculate_scores()
        self.assertEqual(self.player.scores[8], 35)
        self.assertEqual(self.player.scores[16], 35 + 66)

    def test_get_selected_dice_faces(self):
        for i, _ in enumerate(self.player.dices):
            self.player.dices[i].value = 5

        # Select all dice
        for i, _ in enumerate(self.player.dices):
            self.player.dices[i].selected = True

        self.assertEqual([5, 5, 5, 5, 5], self.player.get_selected_dice_faces())

    def test_reset_dice(self):
        # Select all dice
        for i, _ in enumerate(self.player.dices):
            self.player.dices[i].selected = True

        self.player.reset_dice()

        # All dice should be deselected
        for dice in self.player.dices:
            self.assertFalse(dice.selected)

    def test_double_yahtzee(self):
        for i, _ in enumerate(self.player.dices):
            self.player.dices[i].value = 5

        # Simulate that all options have been used before
        # This includes the first yahtzee
        for i, _ in enumerate(self.player.used_rules):
            self.player.used_rules[i] = True

        self.assertTrue(("Yahtzee", 75) in self.player.get_options())

    def test_new_players(self):
        name_one = "Some player"
        name_two = "Another player"

        # run this multiple times because of two randomly selected
        # return statements, otherwise only one will be covered
        for _ in range(10):
            players = new_players(name_one, name_two)

            self.assertIsNotNone(players)
            self.assertIsInstance(players[0], Player)
            self.assertIsInstance(players[1], Player)


            self.assertTrue(players[0].name in (name_one, name_two))
            self.assertTrue(players[1].name in (name_two, name_one))
