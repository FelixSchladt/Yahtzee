#!/usr/bin/python3
# pylint: disable=C
from unittest import TestCase
from rule_generator import multiple,\
                           triplet,\
                           quadrupel,\
                           full_house


class TestRuleGenerator(TestCase):
    def test_multiple(self):
        self.assertEqual(multiple([1, 1, 3, 4, 5], 2), (True, 2))
        self.assertEqual(multiple([1, 2, 3, 4, 5], 1), (True, 1))

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
