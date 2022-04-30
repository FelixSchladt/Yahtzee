#!/usr/bin/python3

# Copyright 2022 Ginthom (https://github.com/Ginthom)

# pylint: disable=C

import platform
from unittest      import TestCase
from unittest.mock import patch
from src.terminal  import terminal,\
                          _posix,\
                          _windows

'''READ:
    Due to terminal containing os-dependant code,
    testing everything is not possible.
    Since these tests were written on a linux based system,
    tests for windows-dependant modules (msvcrt, shutil, ctypes)
    is not possible
'''
class TestRuleGenerator(TestCase):
    def setUp(self):
        self.term = terminal()
        self.do_nothing = lambda *args, **kwargs:\
                          lambda *args, **kwargs: None

    def test_terminal(self):
        if platform.system() in ('Linux', 'FreeBSD'):
            self.assertIsInstance(self.term, _posix)
        else:
            self.assertIsInstance(self.term, _windows)

    def test_getch(self):
        # Size method is dependant on actual terminal size
        # so its hard to define a constant value for it
        self.assertTrue(self.term.rows in range(1, 200))
        self.assertTrue(self.term.columns in range(1, 200))

    def test_posix_getch(self):
        if platform.system() in ('Linux', 'FreeBSD'):
            with patch('sys.stdin.read', return_value='a'):
                self.assertEqual('a', self.term.getch())

        else:
            print("Please run tests for 'terminal' on a linux based OS!")

    def test_posic_clear(self):
        # We can only validate that it does not crash
        # the clear funciotn has to be patched, otherwise
        # the entire test log gets cleared as well
        with patch('os.system', new_callable=self.do_nothing):
            self.term.clear()
