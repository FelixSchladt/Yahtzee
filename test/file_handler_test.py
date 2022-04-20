"""This test file tests the "file_handler" file"""

import unittest

from unittest.mock import patch, mock_open

import file_handler


class FileHandler(unittest.TestCase):
    """
    This class tests the file handler.
    """

    @classmethod
    def test_writetofile(cls):
        """
        This method tests the "save_score" method.
        :rtype: object
        """
        open_mock = mock_open()
        with patch("file_handler.open", open_mock, create=True):
            file_handler.save_score('test-data')

        open_mock.assert_called_with("score_yahtzee.json", "w", encoding="UTF-8")
        open_mock.return_value.write.assert_called_once_with('"test-data"')


if __name__ == '__main__':
    unittest.main()
