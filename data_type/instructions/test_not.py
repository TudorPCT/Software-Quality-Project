from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import NOT, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestNOT(TestCase):
    def test_not_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(5) if reg == Register.eax else None
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()

#If x is 5 (0101 in binary), ~x would be -(0101 + 1), which equals -6.

        not_instruction = NOT(Operand(Register.eax))

        not_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(-6))
