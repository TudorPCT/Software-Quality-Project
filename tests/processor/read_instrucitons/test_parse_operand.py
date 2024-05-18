from unittest import TestCase

from src.data_type.int16 import Int16
from src.processor.processor import Operand, MemoryLocation, Register
from src.processor.read_instructions import InstructionParser


class TestParseOperand(TestCase):

    def test_parse_operand_memory_location(self):
        operand_str = "[10]"
        expected_operand = Operand(MemoryLocation(Int16(10)))
        parsed_operand = InstructionParser.parse_operand(operand_str)
        self.assertIsInstance(parsed_operand, expected_operand.__class__)
        self.assertIsInstance(parsed_operand.data, expected_operand.data.__class__)
        self.assertIsInstance(parsed_operand.data.data, expected_operand.data.data.__class__)
        self.assertEqual(expected_operand.data.data, parsed_operand.data.data)

    def test_parse_operand_constant(self):
        operand_str = "10"
        expected_operand = Operand(Int16(10))
        parsed_operand = InstructionParser.parse_operand(operand_str)
        self.assertIsInstance(parsed_operand, expected_operand.__class__)
        self.assertIsInstance(parsed_operand.data, expected_operand.data.__class__)
        self.assertEqual(expected_operand.data, parsed_operand.data)

    def test_parse_operand_register(self):
        operand_str = "eax"
        expected_operand = Operand(Register["eax"])
        parsed_operand = InstructionParser.parse_operand(operand_str)
        self.assertIsInstance(parsed_operand, expected_operand.__class__)
        self.assertIsInstance(parsed_operand.data, expected_operand.data.__class__)
        self.assertEqual(expected_operand.data, parsed_operand.data)

    def test_parse_operand_register_memory_location(self):
        operand_str = "[eax]"
        expected_operand = Operand(MemoryLocation(Register['eax']))
        parsed_operand = InstructionParser.parse_operand(operand_str)
        self.assertIsInstance(parsed_operand, expected_operand.__class__)
        self.assertIsInstance(parsed_operand.data, expected_operand.data.__class__)
        self.assertIsInstance(parsed_operand.data.data, expected_operand.data.data.__class__)
        self.assertEqual(parsed_operand.data.data, expected_operand.data.data)

    def test_parse_operand_invalid_syntax(self):
        operand_str = "invalid_syntax"
        with self.assertRaises(KeyError):
            InstructionParser.parse_operand(operand_str)

    def test_parse_operand_memory_location_with_comma(self):
        operand_str = "[10],"
        expected_operand = Operand(MemoryLocation(Int16(10)))
        parsed_operand = InstructionParser.parse_operand(operand_str)
        self.assertIsInstance(parsed_operand, expected_operand.__class__)
        self.assertIsInstance(parsed_operand.data, expected_operand.data.__class__)
        self.assertIsInstance(parsed_operand.data.data, expected_operand.data.data.__class__)
        self.assertEqual(parsed_operand.data.data, expected_operand.data.data)

    def test_parse_operand_invalid_register(self):
        operand_str = "invalid_register"
        with self.assertRaises(KeyError):
            InstructionParser.parse_operand(operand_str)
