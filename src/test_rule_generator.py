#!/usr/bin/python3
# pylint: disable=C
from unittest import TestCase
from rule_generator import triplet,\
                           quadrupel


class TestRuleGenerator(TestCase):
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
