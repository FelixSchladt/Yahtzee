#!/usr/bin/python3
# pylint: disable=C
from unittest import TestCase
from rule_generator import triplet


class TestRuleGenerator(TestCase):
    def test_triplet(self):
        self.assertEqual(triplet([1, 1, 1, 4, 5]), (True, 3))
