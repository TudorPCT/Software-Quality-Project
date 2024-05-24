from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.processor.read_instructions import InstructionParser


class TestReadInstructions(TestCase):

    @patch('os.path.isfile')
    @patch('builtins.open')
    def test_read_instructions_from_file(self, mock_open, mock_isfile):
        mock_file_content = [
            "label1:",
            "mov [10], eax",
            "label2:",
            "jmp label1"
        ]

        mock_file = MagicMock()
        mock_file.__enter__.return_value.__iter__.return_value = mock_file_content
        mock_open.return_value = mock_file

        mock_isfile = MagicMock(return_value=True)

        instruction_parser = InstructionParser("test.txt")
        instruction_parser.parse_instruction = MagicMock(return_value="mocked_instruction")

        instructions = instruction_parser.read_instructions_from_file()

        self.assertEqual(len(instructions), 2)
        self.assertEqual(instructions[0], "mocked_instruction")
        self.assertEqual(instructions[1], "mocked_instruction")
