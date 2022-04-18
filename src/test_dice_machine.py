import unittest

from src import dice_machine


class DiceTest(unittest.TestCase):
    def setUp(self):
        """
        :rtype: object
        """
        print("setup Dice_Test")

    def test_keep_rolling_equals(self):
        """
        testcase: no dice are thrown
        """
        print("test: keep rolling")
        actual = dice_machine.Dice.slice_the_dice(self, dice_numbers=[1, 2, 3, 4, 5],
                                                  keep_rolling=[False, False, False, False, False])
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(actual, expected)

    def test_keep_rolling_first(self):
        """
        testcase: dice number 1,2 are thrown
        explenation:    -set dice input 0, if the dice should be thrown
                        -Output can not be 0, because function generates random number between 1 and 6
        """
        actual = dice_machine.Dice.slice_the_dice(self, dice_numbers=[0, 0, 3, 4, 5],
                                                  keep_rolling=[True, True, False, False, False])
        expected = [0, 0, 3, 4, 5]

        self.assertNotEqual(actual[0], 0)
        self.assertNotEqual(actual[1], 0)
        self.assertEqual(actual[2], expected[2])
        self.assertEqual(actual[3], expected[3])
        self.assertEqual(actual[4], expected[4])
