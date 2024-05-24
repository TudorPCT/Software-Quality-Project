from unittest import TestCase
from unittest.mock import Mock, MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.instruction import get_value
from src.memory.main_memory import MainMemory
from src.processor.processor import Processor, Operand, Register, MemoryLocation


class TestGetValue(TestCase):
    def test_operand_with_int16(self):
        cpu = MagicMock(spec=Processor)
        op = Operand(Int16(1234))

        result = get_value(cpu, op)

        self.assertIsInstance(result, Int16)
        self.assertEqual(result.value, 1234)

    def test_operand_with_register(self):
        cpu = MagicMock(spec=Processor)
        register = Register.eax
        op = Operand(register)
        cpu.get_register_val.return_value = Int16(5678)

        result = get_value(cpu, op)

        cpu.get_register_val.assert_called_once_with(register)
        self.assertIsInstance(result, Int16)
        self.assertEqual(result.value, 5678)

    def test_operand_with_memory_location(self):
        cpu = MagicMock(spec=Processor)
        cpu.main_memory = MagicMock(spec=MainMemory)
        address = Int16(100)
        memory_location = MemoryLocation(address)
        inner_value = Int16(7890)
        cpu.main_memory.__getitem__.return_value = inner_value
        op = Operand(memory_location)

        result = get_value(cpu, op)

        self.assertIsInstance(result, Int16)
        self.assertEqual(result.value, 7890)

    def test_nested_memory_location(self):
        cpu = MagicMock(spec=Processor)
        cpu.main_memory = MagicMock(spec=MainMemory)
        address = Int16(200)
        nested_address = Int16(100)
        nested_memory_location = MemoryLocation(nested_address)
        memory_location = MemoryLocation(address)
        inner_op = Operand(nested_memory_location)
        inner_value = Int16(7890)

        cpu.main_memory.__getitem__.side_effect = lambda idx: inner_value if idx == address else inner_op

        op = Operand(memory_location)

        result = get_value(cpu, op)
        self.assertIsInstance(result, Int16)
        self.assertEqual(result.value, 7890)

    def test_invalid_operand(self):
        cpu = MagicMock(spec=Processor)
        op = Operand(None)

        self.assertRaises(AssertionError, lambda: get_value(cpu, op))

