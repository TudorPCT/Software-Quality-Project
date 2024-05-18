from unittest import TestCase
from unittest.mock import MagicMock

from src.data_type.int16 import Int16
from src.memory.instructions.basic_instructions import Mov
from src.processor.processor import Processor, Operand, Register


class TestMov(TestCase):
    def test_mov_register_to_register(self):
        cpu = MagicMock(Processor)

        cpu.set_register_val.side_effect = None
        cpu.get_register_val.side_effect = lambda reg: Int16(100) if reg == Register.ebx else Int16(50)
        cpu.register_ip = Int16()

        mov_instruction = Mov(Operand(Register.eax), Operand(Register.ebx))

        mov_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(100))
