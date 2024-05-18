from unittest import TestCase
from unittest.mock import MagicMock, call, patch
from src.data_type.int16 import Int16
from src.processor.processor import Processor, Operand, Register
from src.memory.instructions.basic_instructions import Cmp
from src.data_type.flag import Flag
import sys

class TestCmp(TestCase):

    def setUp(self):
        if 'src.memory.instructions.basic_instructions' in sys.modules:
            del sys.modules['src.memory.instructions.basic_instructions']

    @patch('src.memory.instructions.instruction.get_value')
    def test_cmp(self, mock_get_value):
        cpu = MagicMock(Processor)
        cpu.register_ip = Int16()

        mock_get_value.side_effect = lambda cpu, operand: Int16(100) if operand == Operand(Register.eax) else Int16(40)

        cpu.flag_eq = Flag(True)
        cpu.flag_neq = Flag(False)
        cpu.flag_lt = Flag(False)
        cpu.flag_gt = Flag(True)
        cpu.flag_lteq = Flag(True)
        cpu.flag_gteq = Flag(True)

        cmp_instruction = Cmp(Operand(Register.eax), Operand(Register.ebx))

        cmp_instruction.run(cpu)

        mock_get_value.assert_has_calls([call(cpu, Operand(Register.eax)), call(cpu, Operand(Register.ebx))])

        self.assertTrue(cpu.flag_eq.value)
        self.assertFalse(cpu.flag_neq.value)
        self.assertFalse(cpu.flag_lt.value)
        self.assertTrue(cpu.flag_gt.value)
        self.assertTrue(cpu.flag_lteq.value)
        self.assertTrue(cpu.flag_gteq.value)