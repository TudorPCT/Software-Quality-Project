from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.util.config_parser import get_data


class Test(TestCase):

    @patch('builtins.open')
    def test_get_data(self, mock_open):
        mock_file_content = [
            "main_memory_size=1024",
            "program_memory_size=1024",
            "keyboard_address=1022",
            "screen_address=830",
            "stack_address=828"
        ]

        mock_file = MagicMock()
        mock_file.__enter__.return_value.__iter__.return_value = mock_file_content
        mock_open.return_value = mock_file

        data = get_data("test.txt")

        self.assertEqual(data, {
            "main_memory_size": 1024,
            "program_memory_size": 1024,
            "keyboard_address": 1022,
            "screen_address": 830,
            "stack_address": 828
        })

    @patch('builtins.open')
    def test_get_data_invalid(self, mock_open):
        mock_file_content = [
            "main_memory_size:1024",
            "program_memory_size=1024",
            "keyboard_address=1022",
            "screen_address=830",
            "stack_address=828"
        ]

        self.mock_file = MagicMock()
        self.mock_file.__enter__.return_value.__iter__.return_value = mock_file_content
        mock_open.return_value = self.mock_file

        with self.assertRaises(AssertionError):
            get_data("test.txt")
