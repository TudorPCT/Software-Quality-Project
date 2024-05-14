from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_intructions import Mov
from src.memory.instructions.jump_instructions import Jmp
from src.memory.instructions.stack_instructions import Ret
from src.processor.processor import Operand, MemoryLocation, Register
from src.processor.read_instructions import InstructionParser


class TestParseInstruction(TestCase):

    def setUp(self) -> None:
        self.instruction_parser = InstructionParser("test.txt")
        self.labels = {"label1": 10, "label2": 20}
        self.instruction_parser.parse_operand = MagicMock(return_value=None)

    def test_parse_instruction_with_operands(self):
        instruction_str = "MOV [10], eax"
        parsed_instruction = self.instruction_parser.parse_instruction(instruction_str, self.labels)
        self.assertIsInstance(parsed_instruction, Mov)

    def test_parse_instruction_jump(self):
        instruction_str = "jmp label1"
        expected_instruction = Jmp(Operand(Int16(10)))  # label1 corresponds to 10
        parsed_instruction = self.instruction_parser.parse_instruction(instruction_str, self.labels)
        self.assertIsInstance(parsed_instruction, expected_instruction.__class__)
        self.assertEqual(expected_instruction.address, parsed_instruction.address)

    def test_parse_instruction_without_operands(self):
        instruction_str = "ret"
        expected_instruction = Ret()
        parsed_instruction = self.instruction_parser.parse_instruction(instruction_str, self.labels)
        self.assertIsInstance(parsed_instruction, expected_instruction.__class__)

    def test_parse_instruction_invalid_format(self):
        instruction_str = "invalid_instruction_format"
        with self.assertRaises(ValueError):
            self.instruction_parser.parse_instruction(instruction_str, self.labels)
