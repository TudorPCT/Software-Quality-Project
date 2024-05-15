from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import SHR, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestSHR(TestCase):
    def test_shr_register_with_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(0b1100) if reg == Register.eax else Int16(2)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()


        shr_instruction = SHR(Operand(Register.eax), Operand(Register.ebx))

        shr_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0b0011))