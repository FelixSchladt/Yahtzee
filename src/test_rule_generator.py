#!/usr/bin/python3
# pylint: disable=C
from unittest import TestCase
from rule_generator import triplet


class TestRuleGenerator(TestCase):
    def test_triplet(self):
        self.assertEqual(triplet([1, 1, 1, 4, 5]), (True, 3))
        self.assertEqual(triplet([5, 2, 3, 5, 5]), (True, 15))
        self.assertEqual(triplet([1, 2, 3, 4, 5]), (False, 0))
        self.assertEqual(triplet([1, 1, 1, 1, 6]), (False, 0))
