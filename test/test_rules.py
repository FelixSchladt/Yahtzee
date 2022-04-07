#!/usr/bin/python3
# pylint: disable=C

# Copyright 2022 Ginthom (https://github.com/Ginthom)


from unittest import TestCase
from src.rules import multiple,\
                         triplet,\
                         quadrupel,\
                         full_house,\
                         small_road,\
                         big_road,\
                         yahtzee,\
                         chance

class TestRuleGenerator(TestCase):
    def test_multiple(self):
        self.assertEqual(multiple([1, 1, 3, 4, 5], 2), (True, 2))
        self.assertEqual(multiple([1, 2, 3, 4, 5], 1), (True, 1))
        self.assertEqual(multiple([1, 2, 3, 4, 5], 3), (False, 0))
        self.assertEqual(multiple([6, 6, 6, 1, 2], 3), (True, 18))

    def test_triplet(self):
        self.assertEqual(triplet([1, 1, 1, 4, 5]), (True, 3))
        self.assertEqual(triplet([5, 2, 3, 5, 5]), (True, 15))
        self.assertEqual(triplet([1, 2, 3, 4, 5]), (False, 0))
        self.assertEqual(triplet([1, 1, 1, 1, 6]), (False, 0))

    def test_quadrupel(self):
        self.assertEqual(quadrupel([1, 1, 1, 1, 6]), (True, 4))
        self.assertEqual(quadrupel([5, 2, 5, 5, 5]), (True, 20))
        self.assertEqual(quadrupel([1, 2, 3, 4, 5]), (False, 0))
        self.assertEqual(quadrupel([1, 1, 1, 1, 1]), (False, 0))
        self.assertEqual(quadrupel([1, 1, 1, 2, 2]), (False, 0))

    def test_full_house(self):
        self.assertEqual(full_house([1, 1, 2, 2, 2]), (True, 25))
        self.assertEqual(full_house([1, 2, 3, 4, 5]), (False, 0))
        self.assertEqual(full_house([1, 1, 2, 3, 4]), (False, 0))
        self.assertEqual(full_house([1, 2, 3, 3, 3]), (False, 0))

    def test_small_road(self):
        self.assertEqual(small_road([1, 2, 3, 4, 1]), (True, 30))
        self.assertEqual(small_road([1, 3, 2, 4, 2]), (True, 30))
        self.assertEqual(small_road([4, 3, 2, 1, 6]), (True, 30))
        self.assertEqual(small_road([6, 5, 4, 3, 6]), (True, 30))
        self.assertEqual(small_road([1, 3, 5, 6, 2]), (False, 0))

    def test_big_road(self):
        self.assertEqual(big_road([1, 2, 3, 4, 5]), (True, 40))
        self.assertEqual(big_road([2, 3, 4, 5, 6]), (True, 40))
        self.assertEqual(big_road([3, 4, 2, 1, 5]), (True, 40))
        self.assertEqual(big_road([1, 2, 3, 4, 6]), (False, 0))

    def test_yahtzee(self):
        self.assertEqual(yahtzee([1, 1, 1, 1, 1]), (True, 50))
        self.assertEqual(yahtzee([1, 2, 3, 4, 5]), (False, 0))
        self.assertEqual(yahtzee([5, 5, 5, 5, 5]), (True, 50))
        self.assertEqual(yahtzee([1, 1, 2, 1, 1]), (False, 0))

    def test_chance(self):
        self.assertEqual(chance([1, 2, 3, 4, 5]), (True, 15))
        self.assertEqual(chance([6, 6, 6, 6, 6]), (True, 30))
        self.assertEqual(chance([3, 6, 1, 2, 3]), (True, 15))
