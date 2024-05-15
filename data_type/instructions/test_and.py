from unittest import TestCase
from unittest.mock import MagicMock
from memory.instructions.basic_intructions import AND, Operand
from processor.processor import Processor, Register
from data_type.int16 import Int16

class TestAND(TestCase):
    def test_and_register_with_register(self):
        cpu = MagicMock(Processor)
        memory = MagicMock()

        cpu.get_register_val.side_effect = lambda reg: Int16(0000) if reg == Register.eax else Int16(1010)
        cpu.set_register_val.side_effect = None
        cpu.register_ip = Int16()


        and_instruction = AND(Operand(Register.eax), Operand(Register.ebx))

        and_instruction.run(cpu)

        cpu.set_register_val.assert_called_once_with(Register.eax, Int16(0000))


