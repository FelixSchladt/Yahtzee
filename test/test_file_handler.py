#!/usr/bin/python3

# pylint: disable=C

from unittest import TestCase
from src.file_handler import save, load


class TestRuleGenerator(TestCase):
    def test_save(self):
        save({"A": "B"}, "test_file")
        with open("test_file.json", "r") as file:
            content = file.read()

        self.assertEqual(content, '{"A": "B"}')

    def test_load(self):
        save({"A": "B"}, "test_file")
        content = load("test_file")
        self.assertEqual(content, {"A": "B"})
