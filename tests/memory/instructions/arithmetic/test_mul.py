import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register


class TestMul(TestCase):

    def setUp(self):
        if 'src.memory.instructions.basic_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.basic_instructions']

    @patch('src.memory.instructions.instruction.get_value')
    @patch('src.memory.instructions.instruction.set_value')
    def test_mul__by_register(self, mock_set_value, mock_get_value):
        from src.memory.instructions.basic_instructions import Mul

        cpu = MagicMock(Processor)

        mock_get_value.return_value = Int16(6)
        mock_set_value.side_effect = None

        cpu.register_ip = Int16()
        cpu.register_eax = Int16(5)

        rh = Operand(Register.ebx)
        mul_instruction = Mul(rh)

        mul_instruction.run(cpu)

        mock_get_value.assert_called_with(cpu, rh)
        mock_set_value.assert_called_with(cpu, Operand(Register.eax), Int16(30))
