from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import XOR, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestXOR(TestCase):
    def test_xor_register_with_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(0b1100) if reg == Register.eax else Int16(0b1010)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()


        xor_instruction = XOR(Operand(Register.eax), Operand(Register.ebx))

        xor_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0b0110))