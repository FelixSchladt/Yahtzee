#!/usr/bin/python3

# pylint: disable=C

import tempfile
import os
from unittest import TestCase 
from src.file_handler import save, load


class TestRuleGenerator(TestCase):
    def test_save(self):
        outfile = tempfile.mkstemp()[1]
        contents = None
        try:
            save({"A": "B"}, outfile)
            contents = open(outfile).read()

        finally:
            os.remove(outfile)

        self.assertEqual(contents, '{"A": B}')
