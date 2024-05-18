from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import Mul, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestMul(TestCase):
    def test_mul_register_by_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(5) if reg == Register.eax else Int16(6)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

        mul_instruction = Mul(Operand(Register.eax), Operand(Register.ebx))

        mul_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(30))