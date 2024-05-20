from unittest import TestCase
from unittest.mock import MagicMock, call, patch
from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register
import sys

class TestNOT(TestCase):

    def setUp(self):
        if 'src.memory.instructions.basic_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.basic_instructions']

    @patch('src.memory.instructions.instruction.get_value')
    @patch('src.memory.instructions.instruction.set_value')
    def test_not(self, mock_set_value, mock_get_value):
        from src.memory.instructions.basic_instructions import NOT

        cpu = MagicMock(Processor)

        mock_get_value.side_effect = lambda cpu, operand: Int16(5) if operand == Operand(Register.eax) else None
        mock_set_value.side_effect = None

        cpu.register_ip = Int16()

        not_instruction = NOT(Operand(Register.eax))

        not_instruction.run(cpu)

        mock_get_value.assert_called_once_with(cpu, Operand(Register.eax))
        mock_set_value.assert_called_once_with(cpu, Operand(Register.eax), Int16(-6))
