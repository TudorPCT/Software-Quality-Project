from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_instructions import SHR
from src.processor.processor import Processor, Register, Operand


class TestSHR(TestCase):
    def test_shr_register_with_register(self):
        cpu = MagicMock(Processor)

        cpu.get_register_val.side_effect = lambda reg: Int16(0b1100) if reg == Register.eax else Int16(2)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        shr_instruction = SHR(Operand(Register.eax), Operand(Register.ebx))

        shr_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0b0011))
