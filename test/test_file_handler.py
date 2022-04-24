"""This test file tests the "file_handler" file"""

import unittest

from unittest.mock import patch, mock_open
from src.file_handler import save, load


class TestRuleGenerator(unittest.TestCase):
    """
    This class tests the file handler.
    """

    @classmethod
    def test_writetofile(cls):
        """
        This method tests the "save" method.
        :rtype: object
        """
        open_mock = mock_open()
        with patch("file_handler.open", open_mock, create=True):
            save({"test-data": "Some_Value"}, "test_save")

        open_mock.assert_called_with("test_save.json", "x", encoding="UTF-8")
        open_mock.return_value.write.assert_called_once_with('{"test-data": "Some_Value"}')


if __name__ == '__main__':
    unittest.main()
