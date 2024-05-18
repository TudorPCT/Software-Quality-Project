from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_instructions import Sub
from src.processor.processor import Processor, Operand, Register


class TestSub(TestCase):
    def test_sub_register_from_register(self):
        cpu = MagicMock(Processor)

        cpu.get_register_val.side_effect = lambda reg: Int16(100) if reg == Register.eax else Int16(40)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        sub_instruction = Sub(Operand(Register.eax), Operand(Register.ebx))

        sub_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(60))
