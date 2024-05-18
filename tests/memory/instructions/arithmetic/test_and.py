from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_instructions import AND
from src.processor.processor import Processor, Operand, Register


class TestAND(TestCase):
    def test_and_register_with_register(self):
        cpu = MagicMock(Processor)

        cpu.get_register_val.side_effect = lambda reg: Int16(0000) if reg == Register.eax else Int16(1010)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        and_instruction = AND(Operand(Register.eax), Operand(Register.ebx))

        and_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0000))
