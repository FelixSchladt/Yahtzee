#!/usr/bin/python3
# Copyright 2022 Felix Schladt (https://github.com/FelixSchladt)

# pylint: disable=C

import os.path
from unittest import TestCase, expectedFailure
from unittest.mock import patch
from src.tui_engine import TuiEngine, category_table, OFFSET, log, draw_dices, RoundsBox
from src.dices import get_dices
from src.exceptions import OutOfBoundsError, InvalidLenghtError

class TestTuiEngine(TestCase):
    def setUp(self):
        self.tui = TuiEngine()
        self.do_nothing = lambda *args, **kwargs:\
                          lambda *args, **kwargs: None

    def test_invalid_terminal_size_invalid_size(self):
        self.tui.display_width = 1
        self.tui.display_height = 1
        with patch('src.tui_engine.TuiEngine.__init__', new_callable=self.do_nothing),\
             self.assertRaises(OutOfBoundsError) as err:
            self.tui.invalid_terminal_size()

        self.assertIsInstance(err.exception, OutOfBoundsError)

    def test_invalid_terminal_size(self):
        with patch.object(TuiEngine, '__init__') as mock_init:
            self.tui.invalid_terminal_size()
            mock_init.assert_called_with()
    
    def test_pixel(self):
        self.tui.pixel(0,0, "A")
        self.assertEqual(self.tui._TuiEngine__grid[1][0], "A\x1b[0m")

    def test_pixel_invalid_char(self):
        with self.assertRaises(InvalidLenghtError) as err:
            self.tui.pixel(1, 1, "Invalid")

        self.assertIsInstance(err.exception, InvalidLenghtError)

    def test_flush(self):
        # flush only prints a list to the terminal
        # We can basically only make sure that the iteration works 
        # without raising an Error
        with patch('builtins.print', new_callable=self.do_nothing):
            self.tui.flush()

    def test_frame(self):
        self.tui.reset_grid()
        self.tui.frame(1, 1, 4, 4)
        self.assertEqual(self.tui._TuiEngine__grid[2][1], "┌\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[2][4], "┐\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[5][1], "└\x1b[0m")
        self.assertEqual(self.tui._TuiEngine__grid[5][4], "┘\x1b[0m")

    def test_dice(self):
        self.tui.reset_grid()
        with self.assertRaises(KeyError) as err:
            self.tui.dice(0,0,7)

        self.assertIsInstance(err.exception, KeyError)

    def test_text(self):
        self.tui.reset_grid()
        self.tui.text((0,0), "test", 3)
        self.assertEqual(self.tui._TuiEngine__grid[1][3], " ")

    def test_text_invalid_text_size(self):
        self.tui.display_width = 1
        with self.assertRaises(OutOfBoundsError) as err:
            self.tui.text((1,1), "This is too long for this display width")

        self.assertIsInstance(err.exception, OutOfBoundsError)

    def test_OutOfBounds(self):
        with self.assertRaises(OutOfBoundsError) as err:
            self.tui.pixel(0, 99999999999999)

        self.assertIsInstance(err.exception, OutOfBoundsError)

    def test_category_table(self):
        category_table(self.tui)
        self.assertEqual(self.tui._TuiEngine__grid[36][self.tui.display_width - OFFSET +1], "T\x1b[0m")

    def test_dices(self):
        draw_dices(self.tui, get_dices())
        self.assertEqual(self.tui._TuiEngine__grid[3][4], "┌\x1b[0m")

    def test_roundsbox(self):
        roundbox = RoundsBox(self.tui)
        self.assertEqual(roundbox.rounds, 2)
        roundbox.text("Test")
        self.assertEqual(roundbox.text.text, "Test")

    def test__reprint(self):
        roundsbox = RoundsBox(self.tui)
        with patch.object(TuiEngine, 'text') as mock_txt:
            roundsbox.draw()
            roundsbox.text.reprint()
            mock_txt.assert_called_with((roundsbox.text.x_pos, roundsbox.text.y_pos),\
                                         roundsbox.text.text,\
                                         roundsbox.text.length,\
                                         roundsbox.text.color)

    def test_reset(self):
        roundsbox = RoundsBox(self.tui)
        roundsbox.rounds = 0
        with patch.object(RoundsBox, 'draw') as mock_draw:
            roundsbox.reset()
            mock_draw.assert_called_with()
            self.assertEqual(roundsbox.rounds, 2)

    def test_roundbox___call__(self):
        roundsbox = RoundsBox(self.tui)
        with patch.object(RoundsBox, 'draw') as mock_draw:
            result = roundsbox()
            mock_draw.assert_called_with()
            self.assertTrue(result)

    def test_roundsbox___call___with_reset(self):
        roundsbox = RoundsBox(self.tui)
        roundsbox.rounds = 1
        with patch.object(RoundsBox, 'reset') as mock_reset:
            result = roundsbox()
            mock_reset.assert_called_with()
            self.assertFalse(result)

    def test_log(self):
        log("Test")
        with open("tui_engine.log", "rb") as file:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
            last_line = file.readline().decode()
        self.assertEqual(last_line, "Test\n")

    def tearDown(self):
        pass
