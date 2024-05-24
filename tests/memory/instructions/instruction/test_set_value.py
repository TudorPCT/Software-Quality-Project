import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.data_type.int16 import Int16
from src.memory.instructions.instruction import set_value
from src.memory.main_memory import MainMemory
from src.processor.processor import Processor, Register, Operand, MemoryLocation


class TestSetValueFunction(TestCase):

    @patch('src.memory.instructions.instruction.get_value')
    def setUp(self, mock_get_value):
        self.cpu = MagicMock(spec=Processor)
        self.cpu.main_memory = MagicMock(spec=MainMemory)
        self.cpu.main_memory.__setitem__.side_effect = None

        self.memory_location = MemoryLocation(Int16(1000))
        mock_get_value.return_value = self.memory_location.data

    def test_set_value_register(self):
        register = Register.eax
        operand = Operand(register)
        value = Int16(1234)

        self.cpu.set_register_val.side_effect = None
        self.cpu.get_register_val.return_value = value

        set_value(self.cpu, operand, value)

        self.cpu.set_register_val.assert_called_with(operand.data, value)

    def test_set_value_memory_location(self):

        operand = Operand(self.memory_location)
        value = Int16(5678)

        self.cpu.main_memory.__getitem__ = MagicMock(return_value=Int16(5678))

        set_value(self.cpu, operand, value)

        self.cpu.main_memory.__setitem__.assert_called_with(self.memory_location.data, value)

    def test_set_value_invalid_operand(self):
        invalid_operand = Operand(Int16())

        with self.assertRaises(AssertionError):
            set_value(self.cpu, invalid_operand, Int16(999))
