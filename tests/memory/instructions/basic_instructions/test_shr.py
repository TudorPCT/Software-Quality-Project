from unittest import TestCase
from unittest.mock import MagicMock, call, patch
from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register
import sys


class TestSHR(TestCase):

    def setUp(self):
        if 'src.memory.instructions.basic_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.basic_instructions']

    @patch('src.memory.instructions.instruction.get_value')
    @patch('src.memory.instructions.instruction.set_value')
    def test_shr(self, mock_set_value, mock_get_value):
        from src.memory.instructions.basic_instructions import SHR

        cpu = MagicMock(Processor)

        mock_get_value.side_effect = lambda cpu, operand: Int16(0b1100) if operand == Operand(Register.eax) else Int16(2)
        mock_set_value.side_effect = None

        cpu.register_ip = Int16()

        shr_instruction = SHR(Operand(Register.eax), Operand(Register.ebx))

        shr_instruction.run(cpu)

        mock_get_value.assert_has_calls([call(cpu, Operand(Register.eax)), call(cpu, Operand(Register.ebx))])
        mock_set_value.assert_called_once_with(cpu, Operand(Register.eax), Int16(0b0011))

