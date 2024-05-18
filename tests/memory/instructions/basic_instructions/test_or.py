from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_instructions import OR
from src.processor.processor import Processor, Operand, Register


class TestOR(TestCase):
    def test_or_register_with_register(self):
        cpu = MagicMock(Processor)

        cpu.get_register_val.side_effect = lambda reg: Int16(0b1100) if reg == Register.eax else Int16(0b1010)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        or_instruction = OR(Operand(Register.eax), Operand(Register.ebx))

        or_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0b1110))

